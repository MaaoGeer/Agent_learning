# AI 智能伴侣

一个基于 [Streamlit](https://streamlit.io/) 和 DeepSeek API 的网页聊天应用。用户可以在侧边栏设置智能体名称和性格，进行流式对话，并在本地保存、加载或删除历史会话。

## 功能

- 使用 DeepSeek `deepseek-flash` 模型生成回复
- 流式显示回复内容
- 自定义智能体名称和性格提示词
- 自动将有内容的会话保存为本地 JSON 文件
- 浏览、加载和删除历史会话
- 新建会话时保留已有聊天记录

## 项目结构

```text
AI_chat/
├── ai_partner.py       # Streamlit 应用入口
├── requirements.txt    # Python 依赖
├── README.md           # 项目说明
└── sessions/           # 运行时创建的本地会话目录
```

`sessions/` 中的文件名采用 `YYYYMMDD_HHMMSS.json` 格式。会话内容、智能体名称和性格设置都会以明文保存在其中。

## 环境要求

- Python 3.9 或更高版本
- 可访问 DeepSeek API 的网络环境
- 有效的 DeepSeek API Key

## 安装

建议在项目目录中创建虚拟环境。

### Windows PowerShell

```powershell
cd E:\Agent_learning\week2\AI_chat
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
cd /path/to/AI_chat
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 配置 API Key

应用从环境变量 `DEEPSEEK_API_KEY` 读取密钥。请勿把真实密钥写入源码或提交到版本控制。

### Windows PowerShell

```powershell
$env:DEEPSEEK_API_KEY="你的_API_Key"
```

### macOS / Linux

```bash
export DEEPSEEK_API_KEY="你的_API_Key"
```

环境变量只对当前终端会话生效。请在设置密钥的同一个终端中启动应用。

## 运行

在项目目录中执行：

```bash
streamlit run ai_partner.py
```

Streamlit 通常会自动打开浏览器；也可以访问终端中显示的地址，默认是 <http://localhost:8501>。

应用使用相对路径 `./sessions` 保存会话，因此应从 `AI_chat` 项目目录启动。若从其他目录启动，会话文件会被写入那个目录下的 `sessions` 文件夹。

## 使用方法

1. 在侧边栏设置“智能体名字”和“智能体性格”。
2. 在页面底部的输入框中发送消息。
3. 应用会逐步显示模型回复，并自动保存有聊天内容的当前会话。
4. 点击侧边栏中的时间戳可加载历史会话。
5. 点击历史会话右侧的删除按钮可删除对应的本地 JSON 文件。
6. 当前会话已有消息时，点击“新建会话”可保存旧会话并开始新会话。

## API 请求说明

项目通过 OpenAI Python SDK 调用 DeepSeek 的 OpenAI 兼容接口，没有使用 OpenAI 平台的 API。

| 配置项 | 当前值或来源 |
| --- | --- |
| API 地址 | `https://api.deepseek.com` |
| API Key | 环境变量 `DEEPSEEK_API_KEY` |
| 模型 | `deepseek-flash` |
| 接口 | `client.chat.completions.create(...)` |
| 输出方式 | 流式输出，`stream=True` |

每次请求会发送以下上下文：

- 根据智能体名称和性格生成的 system 消息
- 当前会话的全部用户消息和助手回复

当前代码没有限制历史消息长度。长会话会增加请求 token 数量、响应时间和可能产生的 API 费用。聊天内容会被发送给 DeepSeek，并同时保存在本机的 `sessions/` 目录中；请勿输入不应发送给模型服务或以明文落盘的敏感信息。

若要更换模型或 API 地址，请修改 `ai_partner.py` 中创建 `OpenAI` 客户端以及发起请求的位置。

## 常见问题

### 提示缺少 `DEEPSEEK_API_KEY`

确认已在当前终端设置环境变量，并从同一终端重新运行 Streamlit。不要在文档、截图或提交记录中暴露密钥。

### 提示 `ModuleNotFoundError`

确认虚拟环境已激活，然后重新安装依赖：

```bash
python -m pip install -r requirements.txt
```

### `st.button()` 不支持 `width` 参数

项目使用了 Streamlit 1.48.0 引入的按钮 `width` 参数。请升级依赖：

```bash
python -m pip install --upgrade "streamlit>=1.48.0"
```

### API 返回鉴权、额度或网络错误

检查 API Key 是否有效、DeepSeek 账户是否有可用额度，以及当前网络是否能访问 `https://api.deepseek.com`。

## 注意事项

- 删除历史会话会直接删除对应的本地 JSON 文件，项目没有回收站或恢复功能。
- 代码目前没有为 API 调用设置异常处理；请求失败时，错误会由 Streamlit 显示。
- 会话 ID 的时间精度为秒。如果在同一秒内创建多个会话，可能出现文件名重复。
- `sessions/` 包含聊天内容。如使用 Git，建议把该目录加入 `.gitignore`。

## 参考资料

- [DeepSeek：首次 API 调用](https://api-docs.deepseek.com/quick_start/agent_integrations/)
- [Streamlit：`st.button` 文档](https://docs.streamlit.io/develop/api-reference/widgets/st.button)

