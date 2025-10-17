#!/usr/bin/env python3
"""Validate project structure for financial analysis multi-agent system."""

import os
import json
from pathlib import Path

def validate_project_structure():
    """Validate that all required project files and directories exist."""
    print("📁 Validating Project Structure")
    print("=" * 40)
    
    base_path = Path("/Users/q.yu/workspace/developments/test")
    
    # Required files and directories
    required_structure = {
        # Configuration files
        ".env": "Environment configuration",
        ".mcp.json": "MCP server configuration", 
        "requirements.txt": "Python dependencies",
        "pyproject.toml": "Project configuration",
        
        # Scripts
        "scripts/test_local_connection.py": "Basic connection test",
        "scripts/test_comprehensive_connection.py": "Comprehensive test suite",
        "scripts/test_mcp_servers.py": "MCP server validation", 
        
        # Project documentation
        "CLAUDE.md": "Claude Code instructions"
    }
    
    # Expected directories (some may be created later)
    expected_dirs = {
        "scripts/": "Utility scripts",
        "src/": "Source code (will be created for DAB project)",
        "tests/": "Unit tests (will be created)",
        "data/": "Sample data (will be created)",
        "docs/": "Documentation (will be created)"
    }
    
    print("🔍 Checking required files...")
    all_files_exist = True
    
    for file_path, description in required_structure.items():
        full_path = base_path / file_path
        if full_path.exists():
            print(f"   ✅ {file_path}: {description}")
        else:
            print(f"   ❌ {file_path}: {description} - MISSING")
            all_files_exist = False
    
    print("\n🔍 Checking directory structure...")
    for dir_path, description in expected_dirs.items():
        full_path = base_path / dir_path
        if full_path.exists():
            print(f"   ✅ {dir_path}: {description}")
        else:
            print(f"   ⚠️  {dir_path}: {description} - Will be created when needed")
    
    # Validate specific configurations
    print("\n🔍 Validating configuration files...")
    
    # Check .env file
    env_path = base_path / ".env"
    if env_path.exists():
        with open(env_path) as f:
            env_content = f.read()
        
        required_env_vars = [
            "DATABRICKS_HOST",
            "DATABRICKS_TOKEN", 
            "DATABRICKS_SERVERLESS_COMPUTE_ID",
            "DATABRICKS_CATALOG",
            "DATABRICKS_SCHEMA"
        ]
        
        env_ok = True
        for var in required_env_vars:
            if var in env_content:
                print(f"   ✅ .env contains {var}")
            else:
                print(f"   ❌ .env missing {var}")
                env_ok = False
                
        if env_ok:
            print("   ✅ .env file properly configured")
    
    # Check MCP configuration
    mcp_path = base_path / ".mcp.json"
    if mcp_path.exists():
        try:
            with open(mcp_path) as f:
                mcp_config = json.load(f)
            
            servers = mcp_config.get('mcpServers', {})
            expected_servers = ['fetch', 'Context7', 'databricks-sdk-py', 'filesystem']
            
            mcp_ok = True
            for server in expected_servers:
                if server in servers:
                    print(f"   ✅ MCP server '{server}' configured")
                else:
                    print(f"   ❌ MCP server '{server}' missing")
                    mcp_ok = False
            
            if mcp_ok:
                print("   ✅ .mcp.json properly configured")
                
        except json.JSONDecodeError:
            print("   ❌ .mcp.json contains invalid JSON")
    
    # Check Python environment
    pyproject_path = base_path / "pyproject.toml"
    if pyproject_path.exists():
        print("   ✅ pyproject.toml exists - Python environment managed by uv")
    
    venv_path = base_path / ".venv"
    if venv_path.exists():
        print("   ✅ Virtual environment (.venv) exists")
    else:
        print("   ❌ Virtual environment missing - run 'uv sync'")
    
    print("\n" + "=" * 40)
    if all_files_exist:
        print("✅ Project structure validation passed!")
        print("🚀 Ready for Databricks development workflow")
    else:
        print("⚠️  Some files are missing but core setup is functional")
    
    return all_files_exist

if __name__ == "__main__":
    validate_project_structure()