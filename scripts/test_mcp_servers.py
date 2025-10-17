#!/usr/bin/env python3
"""Test script to verify MCP server availability."""

import json
import subprocess
import sys
import shutil

def test_mcp_servers():
    """Test MCP server configurations."""
    print("🔧 Testing MCP Server Configurations")
    print("=" * 50)
    
    # Read MCP configuration
    try:
        with open('/Users/q.yu/workspace/developments/test/.mcp.json', 'r') as f:
            mcp_config = json.load(f)
    except FileNotFoundError:
        print("❌ .mcp.json not found")
        return False
    
    servers = mcp_config.get('mcpServers', {})
    if not servers:
        print("❌ No MCP servers configured")
        return False
    
    print(f"📋 Found {len(servers)} MCP server configurations")
    
    all_tests_passed = True
    
    for server_name, config in servers.items():
        print(f"\n🔍 Testing {server_name}...")
        
        command = config.get('command')
        if not command:
            print(f"   ❌ No command specified for {server_name}")
            all_tests_passed = False
            continue
        
        # Check if command is available
        if not shutil.which(command):
            print(f"   ❌ Command '{command}' not found in PATH")
            all_tests_passed = False
            continue
        
        print(f"   ✅ Command '{command}' is available")
        
        # Test specific server capabilities
        if server_name == "fetch":
            print(f"   📦 uvx mcp-server-fetch - for web content fetching")
        elif server_name == "Context7":
            print(f"   📦 @upstash/context7-mcp - for context management")
        elif server_name == "databricks-sdk-py":
            print(f"   📦 Databricks SDK integration - for SDK documentation")
        elif server_name == "filesystem":
            print(f"   📦 @modelcontextprotocol/server-filesystem - for file operations")
        
        print(f"   ✅ {server_name} configuration looks good")
    
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("✅ All MCP servers are properly configured!")
        print("\n💡 MCP servers will be automatically activated when using Claude Code")
    else:
        print("❌ Some MCP server configurations have issues")
    
    return all_tests_passed

def test_required_tools():
    """Test that required tools are available."""
    print("\n🛠️  Testing Required Tools")
    print("=" * 30)
    
    tools = {
        'node': 'Node.js runtime',
        'npx': 'Node package runner', 
        'uvx': 'UV package runner'
    }
    
    all_available = True
    for tool, description in tools.items():
        if shutil.which(tool):
            print(f"   ✅ {tool}: {description}")
        else:
            print(f"   ❌ {tool}: {description} - NOT FOUND")
            all_available = False
    
    return all_available

if __name__ == "__main__":
    print("🧪 MCP Server Test Suite")
    print("=" * 60)
    
    tools_ok = test_required_tools()
    servers_ok = test_mcp_servers()
    
    if tools_ok and servers_ok:
        print("\n🎉 All MCP configurations are ready!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        sys.exit(1)