# MCP Agent - Multi-Agent System

Một hệ thống multi-agent Python sử dụng Google ADK (Agent Development Kit) với GitHub Models để tạo ra các trợ lý AI thông minh có thể làm việc độc lập hoặc kết hợp với nhau.

## Tính năng

- **Multi-Agent Architecture**: Hỗ trợ nhiều agent, mỗi agent có model, functions và session management riêng
- **Agent Orchestration**: Điều phối và kết hợp nhiều agent để xử lý các tác vụ phức tạp
- **Modular Design**: Cấu trúc module cho phép dễ dàng thêm agent mới
- Sử dụng GitHub Models thông qua LiteLlm
- Tích hợp với Google ADK
- Cấu hình linh hoạt thông qua environment variables

## Cấu trúc dự án

```
MCP/
├── agents/
│   ├── __init__.py
│   ├── base/                    # Base classes
│   │   ├── __init__.py
│   │   ├── agent_base.py       # Base agent class
│   │   ├── model_base.py       # Base model class
│   │   └── session_base.py     # Base session class
│   ├── orchestrator.py          # Agent orchestrator for coordination
│   └── weather_agent/           # Weather Agent example
│       ├── __init__.py
│       ├── agent.py            # Agent implementation
│       ├── model.py            # Model configuration
│       ├── functions.py        # Agent functions/tools
│       └── session.py          # Session management
├── shared/                      # Shared utilities
│   ├── __init__.py
│   ├── config.py               # Shared configuration
│   └── session_manager.py      # Shared session manager
├── utils/                       # Utility functions
│   └── __init__.py
├── examples/                    # Example scripts
│   ├── __init__.py
│   ├── basic_usage.py          # Basic usage examples
│   └── shared_session_example.py  # Shared session examples
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variables example
└── README.md                   # File này
```

## Cài đặt

1. Clone repository này:
```bash
git clone https://github.com/yourusername/MCP.git
cd MCP
```

2. Tạo virtual environment (khuyến nghị):
```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Thiết lập environment variables:
```bash
cp .env.example .env
# Chỉnh sửa .env với các giá trị của bạn
export GITHUB_TOKEN="your_github_token_here"
```

## Sử dụng

### Sử dụng một agent đơn lẻ

```python
from agents.weather_agent import WeatherAgent

# Khởi tạo agent
weather_agent = WeatherAgent()

# Lấy agent instance
agent = weather_agent.get_agent()

# Lấy runner để thực thi
runner = weather_agent.get_runner()

# Sử dụng agent
response = await runner.run("What's the weather in Tokyo?")
print(response)
```

### Sử dụng Agent Orchestrator

```python
from agents import AgentOrchestrator, WeatherAgent

# Khởi tạo orchestrator
orchestrator = AgentOrchestrator()

# Đăng ký agents
weather_agent = WeatherAgent()
orchestrator.register_agent(
    weather_agent,
    capabilities=["weather", "temperature", "climate"]
)

# Tìm agent phù hợp
agent = orchestrator.route_request("What's the weather today?")

# Hoặc kết hợp nhiều agents
combined = orchestrator.combine_agents(["weather_agent", "other_agent"])
```

### Tạo agent mới

1. Tạo thư mục cho agent mới trong `agents/`:
```bash
mkdir agents/my_new_agent
```

2. Tạo các file cần thiết:
- `model.py`: Cấu hình model
- `functions.py`: Các functions/tools của agent
- `session.py`: Quản lý session
- `agent.py`: Implementation của agent

3. Example structure:
```python
# agents/my_new_agent/agent.py
from agents.base.agent_base import BaseAgent
from agents.my_new_agent.model import MyModel
from agents.my_new_agent.functions import MyFunctions
from agents.my_new_agent.session import MySession

class MyNewAgent(BaseAgent):
    def __init__(self):
        # Initialize model, functions, session
        # Call super().__init__() with appropriate parameters
        pass
    
    def initialize(self):
        # Initialize agent instance
        pass
    
    def get_agent(self):
        # Return initialized agent
        pass
```

## Cấu trúc Agent

Mỗi agent gồm 3 thành phần chính:

1. **Model**: Cấu hình và khởi tạo LLM model
   - Kế thừa từ `BaseModel`
   - Implement `initialize()` và `get_model()`

2. **Functions**: Các tools/functions mà agent có thể sử dụng
   - Chứa các functions độc lập
   - Method `get_all_functions()` trả về danh sách functions

3. **Session Management**: Quản lý session và runner
   - Kế thừa từ `BaseSession`
   - Implement `initialize()`, `create_session()`, và `get_runner()`

## Shared Session & Runner

Hệ thống hỗ trợ **dùng chung SessionService** giữa các agents để tối ưu tài nguyên:

### Shared SessionService

- `SessionService` có thể được **dùng chung** giữa tất cả agents
- `SharedSessionManager` là singleton quản lý session service chung
- Mặc định tất cả agents đều sử dụng shared session

### Runner

- `Runner` được tạo **cho từng agent cụ thể** (không thể dùng chung)
- Tuy nhiên, các runners có thể **dùng chung cùng một SessionService**
- Runners có thể được **cache** để tránh tạo lại nhiều lần cho cùng một agent

### Sử dụng Shared Session

```python
from agents import WeatherAgent
from shared import SharedSessionManager

# Agent mặc định sử dụng shared session
weather_agent = WeatherAgent()
runner = weather_agent.get_runner()  # Dùng shared SessionService

# Hoặc sử dụng SharedSessionManager trực tiếp
shared_manager = SharedSessionManager()
shared_manager.initialize(app_name="my_app")

# Tạo session
session = await shared_manager.create_session(user_id="user_1")

# Lấy runner với cache
runner = shared_manager.get_runner(agent, use_cache=True)
```

### Sử dụng Isolated Session

Nếu muốn agent có session riêng:

```python
from agents.weather_agent import WeatherAgent, WeatherSession

# Tạo session riêng
session = WeatherSession(use_shared_session=False)
weather_agent = WeatherAgent(session_config=..., use_shared_session=False)
```

Xem thêm ví dụ trong `examples/shared_session_example.py`

## Yêu cầu

- Python 3.7+
- GitHub token để sử dụng GitHub Models
- Các dependencies được liệt kê trong `requirements.txt`

## Dependencies

```
google-adk
python-dotenv
```

## Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request nếu bạn có ý tưởng cải thiện dự án.

## License

MIT License
