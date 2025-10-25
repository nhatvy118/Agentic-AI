# MCP Agent

Một agent Python sử dụng Google ADK (Agent Development Kit) với GitHub Models để tạo ra một trợ lý AI thông minh.

## Tính năng

- Sử dụng GitHub Models thông qua LiteLlm
- Tích hợp với Google ADK
- Hỗ trợ GPT-4.1-mini model
- Cấu hình linh hoạt thông qua environment variables

## Cài đặt

1. Clone repository này:
```bash
git clone https://github.com/yourusername/MCP.git
cd MCP
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Thiết lập environment variables:
```bash
export GITHUB_TOKEN="your_github_token_here"
```

## Sử dụng

```python
from my_agent.agent import root_agent

# Sử dụng agent
response = root_agent.ask("Xin chào, bạn có thể giúp gì cho tôi?")
print(response)
```

## Cấu trúc dự án

```
MCP/
├── my_agent/
│   ├── __init__.py
│   └── agent.py          # File chính chứa agent configuration
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # File này
```

## Yêu cầu

- Python 3.7+
- GitHub token để sử dụng GitHub Models
- Các dependencies được liệt kê trong requirements.txt

## Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request nếu bạn có ý tưởng cải thiện dự án.

## License

MIT License
