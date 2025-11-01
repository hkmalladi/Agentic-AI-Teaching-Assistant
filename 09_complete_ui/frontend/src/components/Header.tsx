import { motion } from 'framer-motion';
import { Menu, GraduationCap, Sparkles } from 'lucide-react';

interface HeaderProps {
  sidebarOpen: boolean;
  onToggleSidebar: () => void;
}

const Header = ({ sidebarOpen, onToggleSidebar }: HeaderProps) => {
  return (
    <motion.header
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ type: 'spring', damping: 20 }}
      className="glass-effect border-b border-white/20 px-6 py-4"
    >
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          {/* Menu Button */}
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={onToggleSidebar}
            className="p-2 rounded-xl hover:bg-white/50 transition-colors"
            aria-label="Toggle sidebar"
          >
            <Menu className="w-6 h-6 text-slate-700" />
          </motion.button>

          {/* Logo and Title */}
          <div className="flex items-center gap-3">
            <motion.div
              animate={{
                rotate: [0, 10, -10, 10, 0],
              }}
              transition={{
                duration: 2,
                repeat: Infinity,
                repeatDelay: 3,
              }}
              className="relative"
            >
              <GraduationCap className="w-8 h-8 text-indigo-600" />
              <motion.div
                animate={{
                  scale: [1, 1.2, 1],
                  opacity: [0.5, 1, 0.5],
                }}
                transition={{
                  duration: 2,
                  repeat: Infinity,
                }}
                className="absolute -top-1 -right-1"
              >
                <Sparkles className="w-4 h-4 text-yellow-500" />
              </motion.div>
            </motion.div>
            
            <div>
              <h1 className="text-2xl font-bold gradient-text">
                AI Teaching Assistant
              </h1>
              <p className="text-xs text-slate-500">
                Built from scratch with React + TypeScript
              </p>
            </div>
          </div>
        </div>

        {/* Status Indicator */}
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ delay: 0.5, type: 'spring' }}
          className="flex items-center gap-2 px-4 py-2 rounded-full bg-green-50 border border-green-200"
        >
          <motion.div
            animate={{
              scale: [1, 1.2, 1],
            }}
            transition={{
              duration: 2,
              repeat: Infinity,
            }}
            className="w-2 h-2 bg-green-500 rounded-full"
          />
          <span className="text-sm font-medium text-green-700">Online</span>
        </motion.div>
      </div>
    </motion.header>
  );
};

export default Header;

