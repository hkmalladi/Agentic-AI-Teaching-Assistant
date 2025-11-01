import { motion } from 'framer-motion';
import { User, Bot, MessageCircle, FileQuestion, Brain } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { Message } from '../types';

interface ChatMessageProps {
  message: Message;
  index: number;
}

const ChatMessage = ({ message, index }: ChatMessageProps) => {
  const isUser = message.role === 'user';

  const getAgentInfo = (agent?: string) => {
    switch (agent) {
      case 'chat':
        return {
          icon: <MessageCircle className="w-4 h-4" />,
          label: 'Chat Agent',
          color: 'bg-blue-100 text-blue-700 border-blue-200',
        };
      case 'quiz':
        return {
          icon: <FileQuestion className="w-4 h-4" />,
          label: 'Quiz Agent',
          color: 'bg-green-100 text-green-700 border-green-200',
        };
      case 'explanation':
        return {
          icon: <Brain className="w-4 h-4" />,
          label: 'Explanation Agent',
          color: 'bg-purple-100 text-purple-700 border-purple-200',
        };
      default:
        return null;
    }
  };

  const agentInfo = !isUser ? getAgentInfo(message.agent) : null;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      transition={{
        type: 'spring',
        damping: 25,
        stiffness: 200,
        delay: index * 0.05,
      }}
      className={`flex gap-4 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}
    >
      {/* Avatar */}
      <motion.div
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        transition={{ delay: index * 0.05 + 0.1, type: 'spring' }}
        className={`flex-shrink-0 w-10 h-10 rounded-xl flex items-center justify-center ${
          isUser
            ? 'bg-gradient-to-br from-indigo-500 to-blue-500 text-white shadow-lg shadow-indigo-500/30'
            : 'bg-gradient-to-br from-slate-100 to-slate-200 text-slate-700 border border-slate-300'
        }`}
      >
        {isUser ? <User className="w-5 h-5" /> : <Bot className="w-5 h-5" />}
      </motion.div>

      {/* Message Content */}
      <div className={`flex-1 max-w-3xl ${isUser ? 'items-end' : 'items-start'} flex flex-col gap-2`}>
        {/* Agent Badge */}
        {agentInfo && (
          <motion.div
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.05 + 0.2 }}
            className={`agent-badge border ${agentInfo.color}`}
          >
            {agentInfo.icon}
            <span>{agentInfo.label}</span>
          </motion.div>
        )}

        {/* Message Bubble */}
        <motion.div
          initial={{ scale: 0.9 }}
          animate={{ scale: 1 }}
          transition={{ delay: index * 0.05 + 0.15 }}
          className={`message-bubble ${
            isUser
              ? 'bg-gradient-to-br from-indigo-600 to-blue-600 text-white ml-auto'
              : 'glass-effect text-slate-800'
          }`}
        >
          {isUser ? (
            <p className="whitespace-pre-wrap leading-relaxed">{message.content}</p>
          ) : (
            <div className="prose prose-sm max-w-none prose-slate">
              <ReactMarkdown
                components={{
                  code({ node, inline, className, children, ...props }) {
                    const match = /language-(\w+)/.exec(className || '');
                    return !inline && match ? (
                      <SyntaxHighlighter
                        style={oneDark}
                        language={match[1]}
                        PreTag="div"
                        className="rounded-xl !mt-2 !mb-2"
                        {...props}
                      >
                        {String(children).replace(/\n$/, '')}
                      </SyntaxHighlighter>
                    ) : (
                      <code
                        className="bg-slate-200 text-slate-800 px-1.5 py-0.5 rounded text-sm"
                        {...props}
                      >
                        {children}
                      </code>
                    );
                  },
                  p: ({ children }) => (
                    <p className="mb-3 last:mb-0 leading-relaxed">{children}</p>
                  ),
                  ul: ({ children }) => (
                    <ul className="list-disc list-inside mb-3 space-y-1">{children}</ul>
                  ),
                  ol: ({ children }) => (
                    <ol className="list-decimal list-inside mb-3 space-y-1">{children}</ol>
                  ),
                  h1: ({ children }) => (
                    <h1 className="text-xl font-bold mb-2 mt-4 first:mt-0">{children}</h1>
                  ),
                  h2: ({ children }) => (
                    <h2 className="text-lg font-bold mb-2 mt-3 first:mt-0">{children}</h2>
                  ),
                  h3: ({ children }) => (
                    <h3 className="text-base font-bold mb-2 mt-2 first:mt-0">{children}</h3>
                  ),
                }}
              >
                {message.content}
              </ReactMarkdown>
            </div>
          )}
        </motion.div>

        {/* Timestamp */}
        <motion.span
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: index * 0.05 + 0.3 }}
          className="text-xs text-slate-400 px-2"
        >
          {new Date(message.timestamp).toLocaleTimeString()}
        </motion.span>
      </div>
    </motion.div>
  );
};

export default ChatMessage;

