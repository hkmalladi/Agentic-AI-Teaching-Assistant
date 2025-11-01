/**
 * Type definitions for the AI Teaching Assistant
 */

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  agent?: string;
  timestamp: string;
}

export interface ChatResponse {
  response: string;
  agent: string;
  timestamp: string;
}

export interface Agent {
  name: string;
  description: string;
  icon: string;
  color: string;
}

export interface AgentsResponse {
  agents: Agent[];
}

