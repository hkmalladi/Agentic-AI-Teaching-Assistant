/**
 * API client for communicating with the FastAPI backend
 */

import axios from 'axios';
import { ChatResponse, AgentsResponse } from './types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Send a chat message to the AI
 */
export const sendMessage = async (message: string): Promise<ChatResponse> => {
  const response = await api.post<ChatResponse>('/api/chat', {
    message,
    conversation_history: [],
  });
  return response.data;
};

/**
 * Get information about available agents
 */
export const getAgents = async (): Promise<AgentsResponse> => {
  const response = await api.get<AgentsResponse>('/api/agents');
  return response.data;
};

/**
 * Health check
 */
export const healthCheck = async (): Promise<{ status: string; message: string }> => {
  const response = await api.get('/health');
  return response.data;
};

export default api;

