import urllib.request
import os

folder = os.path.join(os.path.dirname(__file__), "public", "images")
if not os.path.exists(folder):
    os.makedirs(folder)

# Skills with solid white background and black text for maximum visibility in dark theme
skills = {
    "react_native.png": "https://placehold.co/512/ffffff/000000/png?text=React%5CnNative",
    "react.png": "https://placehold.co/512/ffffff/000000/png?text=ReactJS",
    "javascript.png": "https://placehold.co/512/ffffff/000000/png?text=JavaScript",
    "typescript.png": "https://placehold.co/512/ffffff/000000/png?text=TypeScript",
    "shopify.png": "https://placehold.co/512/ffffff/000000/png?text=Shopify",
    "python.png": "https://placehold.co/512/ffffff/000000/png?text=Python",
    "flask.png": "https://placehold.co/512/ffffff/000000/png?text=Flask",
    "dotnet.png": "https://placehold.co/512/ffffff/000000/png?text=.NET+(C%23)",
    "docker.png": "https://placehold.co/512/ffffff/000000/png?text=Docker",
    "mysql.png": "https://placehold.co/512/ffffff/000000/png?text=MySQL",
    "mongodb.png": "https://placehold.co/512/ffffff/000000/png?text=MongoDB",
    "openai.png": "https://placehold.co/512/ffffff/000000/png?text=OpenAI",
    "langchain.png": "https://placehold.co/512/ffffff/000000/png?text=LangChain",
    "langgraph.png": "https://placehold.co/512/ffffff/000000/png?text=LangGraph",
    "mcp.png": "https://placehold.co/512/ffffff/000000/png?text=MCP%5CnServers",
    "rag.png": "https://placehold.co/512/ffffff/000000/png?text=RAG%5CnPipelines",
    "ollama.png": "https://placehold.co/512/ffffff/000000/png?text=Ollama",
    "n8n.png": "https://placehold.co/512/ffffff/000000/png?text=n8n",
    "ai_agents.png": "https://placehold.co/512/ffffff/000000/png?text=AI%5CnAgents",
    "system_design.png": "https://placehold.co/512/ffffff/000000/png?text=System%5CnDesign",
    "microservices.png": "https://placehold.co/512/ffffff/000000/png?text=Microserv%5Cnices",
    "huggingface.png": "https://placehold.co/512/ffffff/000000/png?text=Hugging%5CnFace"
}

for name, url in skills.items():
    print(f"Downloading {name} from {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(os.path.join(folder, name), 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"Error downloading {name}: {e}")

print("Done!")
