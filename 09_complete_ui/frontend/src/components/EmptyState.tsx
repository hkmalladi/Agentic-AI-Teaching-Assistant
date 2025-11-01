import { motion } from 'framer-motion';
import { MessageCircle, FileQuestion, Brain, Sparkles } from 'lucide-react';

const EmptyState = () => {
  const features = [
    {
      icon: <MessageCircle className="w-6 h-6" />,
      title: 'Chat',
      description: 'Ask questions and have natural conversations',
      color: 'from-blue-500 to-cyan-500',
    },
    {
      icon: <FileQuestion className="w-6 h-6" />,
      title: 'Quiz',
      description: 'Generate practice problems and quizzes',
      color: 'from-green-500 to-emerald-500',
    },
    {
      icon: <Brain className="w-6 h-6" />,
      title: 'Explain',
      description: 'Get detailed explanations of complex concepts',
      color: 'from-purple-500 to-pink-500',
    },
  ];

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center px-4">
      {/* Animated Icon */}
      <motion.div
        initial={{ scale: 0, rotate: -180 }}
        animate={{ scale: 1, rotate: 0 }}
        transition={{
          type: 'spring',
          damping: 15,
          stiffness: 100,
        }}
        className="relative mb-8"
      >
        <motion.div
          animate={{
            rotate: [0, 360],
          }}
          transition={{
            duration: 20,
            repeat: Infinity,
            ease: 'linear',
          }}
          className="absolute inset-0 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-full blur-2xl opacity-30"
        />
        <div className="relative bg-gradient-to-br from-indigo-600 to-blue-600 p-8 rounded-3xl shadow-2xl">
          <Sparkles className="w-16 h-16 text-white" />
        </div>
      </motion.div>

      {/* Welcome Text */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="mb-8"
      >
        <h2 className="text-4xl font-bold gradient-text mb-3">
          Welcome to AI Teaching Assistant
        </h2>
        <p className="text-lg text-slate-600 max-w-2xl">
          Your intelligent learning companion powered by GPT-4. Ask questions, generate quizzes, or get detailed explanations.
        </p>
      </motion.div>

      {/* Features Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl w-full mb-8">
        {features.map((feature, index) => (
          <motion.div
            key={feature.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 + index * 0.1 }}
            whileHover={{ scale: 1.05, y: -5 }}
            className="glass-effect p-6 rounded-2xl"
          >
            <motion.div
              whileHover={{ rotate: [0, -10, 10, -10, 0] }}
              transition={{ duration: 0.5 }}
              className={`w-12 h-12 rounded-xl bg-gradient-to-br ${feature.color} text-white flex items-center justify-center mb-4 shadow-lg`}
            >
              {feature.icon}
            </motion.div>
            <h3 className="text-lg font-semibold text-slate-800 mb-2">
              {feature.title}
            </h3>
            <p className="text-sm text-slate-600">
              {feature.description}
            </p>
          </motion.div>
        ))}
      </div>

      {/* Call to Action */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6 }}
        className="glass-effect px-6 py-4 rounded-2xl"
      >
        <p className="text-sm text-slate-600">
          💡 <span className="font-medium">Pro tip:</span> The AI automatically routes your question to the best agent for the job!
        </p>
      </motion.div>

      {/* Floating Particles */}
      {[...Array(5)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute w-2 h-2 bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full"
          animate={{
            x: [0, Math.random() * 100 - 50],
            y: [0, Math.random() * 100 - 50],
            opacity: [0, 1, 0],
          }}
          transition={{
            duration: 3 + Math.random() * 2,
            repeat: Infinity,
            delay: i * 0.5,
          }}
          style={{
            left: `${20 + i * 15}%`,
            top: `${30 + Math.random() * 40}%`,
          }}
        />
      ))}
    </div>
  );
};

export default EmptyState;

