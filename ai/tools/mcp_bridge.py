import subprocess
import json
import os

def call_mcp_jira_ticket(summary, description, priority, assignee_group):
    """
    Envoie une requête JSON-RPC au serveur MCP Atlassian via STDIO.
    """
    # Chemin vers ton dossier mcp-nodejs-atlassian
    mcp_dir = os.path.join(os.getcwd(), "mcp-nodejs-atlassian")
    
    # Construction de la requête JSON-RPC demandée par ton serveur
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "jira_create_issue",
            "arguments": {
                "projectKey": "KAN", # Clé projet de ton image
                "issueType": "Task",
                "summary": summary,
                "description": f"RESPONSABLE : {assignee_group}\nPRIORITÉ : {priority}\n\nDETAILS :\n{description}"
            }
        }
    }

    try:
        # On lance 'node dist/index.js' comme dans ton script Node
        process = subprocess.Popen(
            ["node", "dist/index.js"],
            cwd=mcp_dir,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # 📤 Envoyer vers MCP (stdin)
        stdout, stderr = process.communicate(input=json.dumps(request) + "\n")

        if process.returncode == 0:
            return stdout # C'est la réponse MCP RESPONSE
        else:
            return f"Erreur MCP: {stderr}"

    except Exception as e:
        return f"Erreur de connexion: {str(e)}"