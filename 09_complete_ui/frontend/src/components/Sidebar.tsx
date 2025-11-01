import { motion } from 'framer-motion';
import { Trash2, Info, Lightbulb, MessageCircle, FileQuestion, Brain } from 'lucide-react';
import { Agent } from '../types';

interface SidebarProps {
  agents: Agent[];
  onClearChat: () => void;
  messageCount: number;
}

const Sidebar = ({ agents, onClearChat, messageCount }: SidebarProps) => {
  const getAgentIcon = (agentName: string) => {
    switch (agentName) {
      case 'chat':
        return <MessageCircle className="w-5 h-5" />;
      case 'quiz':
        return <FileQuestion className="w-5 h-5" />;
      case 'explanation':
        return <Brain className="w-5 h-5" />;
      default:
        return <MessageCircle className="w-5 h-5" />;
    }
  };

  const getAgentColor = (color: string) => {
    const colors: Record<string, string> = {
      blue: 'bg-blue-50 border-blue-200 text-blue-700',
      green: 'bg-green-50 border-green-200 text-green-700',
      purple: 'bg-purple-50 border-purple-200 text-purple-700',
    };
    return colors[color] || colors.blue;
  };

  const examplePrompts = [
    {
      category: 'Chat',
      icon: <MessageCircle className="w-4 h-4" />,
      prompts: [
        'What is Python?',
        'How are you today?',
        'Tell me about AI',
      ],
    },
    {
      category: 'Quiz',
      icon: <FileQuestion className="w-4 h-4" />,
      prompts: [
        'Create a quiz on Python',
        'Generate practice problems',
        'Test me on machine learning',
      ],
    },
    {
      category: 'Explanation',
      icon: <Brain className="w-4 h-4" />,
      prompts: [
        'Explain machine learning',
        'What is photosynthesis?',
        'How does the internet work?',
      ],
    },
  ];

  return (
    <motion.aside
      className="h-screen glass-effect border-r border-white/20 flex flex-col"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      {/* Sidebar Header */}
      <div className="p-6 border-b border-white/20">
        <div className="flex items-center gap-2 mb-2">
          <Info className="w-5 h-5 text-indigo-600" />
          <h2 className="text-lg font-semibold text-slate-800">About</h2>
        </div>
        <p className="text-sm text-slate-600 leading-relaxed">
          This AI Teaching Assistant uses specialized agents to help you learn effectively.
        </p>
      </div>

      {/* Agents Section */}
      <div className="p-6 border-b border-white/20">
        <h3 className="text-sm font-semibold text-slate-700 mb-3 flex items-center gap-2">
          <Lightbulb className="w-4 h-4 text-yellow-500" />
          Available Agents
        </h3>
        <div className="space-y-2">
          {agents.map((agent, index) => (
            <motion.div
              key={agent.name}
              initial={{ x: -20, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              transition={{ delay: index * 0.1 }}
              className={`p-3 rounded-xl border ${getAgentColor(agent.color)} transition-all hover:shadow-md`}
            >
              <div className="flex items-start gap-3">
                <div className="mt-0.5">
                  {getAgentIcon(agent.name)}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-lg">{agent.icon}</span>
                    <span className="font-medium text-sm capitalize">
                      {agent.name}
                    </span>
                  </div>
                  <p className="text-xs opacity-80 leading-relaxed">
                    {agent.description}
                  </p>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Example Prompts */}
      <div className="flex-1 overflow-y-auto p-6">
        <h3 className="text-sm font-semibold text-slate-700 mb-3 flex items-center gap-2">
          <MessageCircle className="w-4 h-4 text-indigo-500" />
          Try These Examples
        </h3>
        <div className="space-y-4">
          {examplePrompts.map((category, index) => (
            <motion.div
              key={category.category}
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.3 + index * 0.1 }}
            >
              <div className="flex items-center gap-2 mb-2">
                {category.icon}
                <h4 className="text-xs font-semibold text-slate-600">
                  {category.category}
                </h4>
              </div>
              <div className="space-y-1.5">
                {category.prompts.map((prompt, i) => (
                  <motion.div
                    key={i}
                    whileHover={{ x: 4 }}
                    className="text-xs text-slate-600 hover:text-indigo-600 cursor-pointer p-2 rounded-lg hover:bg-white/50 transition-all"
                  >
                    • {prompt}
                  </motion.div>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Clear Chat Button */}
      <div className="p-6 border-t border-white/20">
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={onClearChat}
          disabled={messageCount === 0}
          className={`w-full flex items-center justify-center gap-2 px-4 py-3 rounded-xl font-medium transition-all ${
            messageCount === 0
              ? 'bg-slate-100 text-slate-400 cursor-not-allowed'
              : 'bg-gradient-to-r from-red-500 to-pink-500 text-white hover:shadow-lg hover:shadow-red-500/30'
          }`}
        >
          <Trash2 className="w-4 h-4" />
          Clear Chat ({messageCount})
        </motion.button>
      </div>
    </motion.aside>
  );
};

export default Sidebar;

