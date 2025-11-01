# AI Teaching Assistant - React Frontend

Beautiful, modern React + TypeScript + Tailwind CSS frontend for the AI Teaching Assistant.

## ✨ Features

- 🎨 **Beautiful UI** - Modern, gradient-based design with glass morphism effects
- ⚡ **Smooth Animations** - Framer Motion for fluid, professional animations
- 📱 **Responsive** - Works perfectly on desktop, tablet, and mobile
- 🎯 **Type-Safe** - Full TypeScript support for better development experience
- 🎨 **Tailwind CSS** - Utility-first CSS for rapid UI development
- 💬 **Real-time Chat** - Instant messaging with the AI
- 🤖 **Agent Indicators** - Visual feedback showing which agent is responding
- 📝 **Markdown Support** - Rich text formatting and code syntax highlighting
- 🌈 **Dark Code Blocks** - Beautiful syntax highlighting for code snippets

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm/yarn/pnpm
- Backend API running on `http://localhost:8000`

### Installation

```bash
# Install dependencies
npm install

# Copy environment file
cp .env.example .env

# Start development server
npm run dev
```

The app will be available at `http://localhost:3000`

## 📦 Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── Header.tsx       # Top navigation bar
│   │   ├── Sidebar.tsx      # Left sidebar with info
│   │   ├── ChatInterface.tsx # Main chat area
│   │   ├── ChatMessage.tsx  # Individual message component
│   │   └── EmptyState.tsx   # Welcome screen
│   ├── api.ts              # API client for backend
│   ├── types.ts            # TypeScript type definitions
│   ├── App.tsx             # Main app component
│   ├── main.tsx            # Entry point
│   └── index.css           # Global styles
├── public/                 # Static assets
├── index.html             # HTML template
├── package.json           # Dependencies
├── tsconfig.json          # TypeScript config
├── tailwind.config.js     # Tailwind CSS config
└── vite.config.ts         # Vite config
```

## 🎨 Design System

### Colors

- **Primary**: Indigo/Blue gradient
- **Chat Agent**: Blue tones
- **Quiz Agent**: Green tones
- **Explanation Agent**: Purple tones

### Components

- **Glass Effect**: Frosted glass morphism with backdrop blur
- **Gradient Text**: Smooth color transitions for headings
- **Message Bubbles**: Rounded, shadowed containers
- **Agent Badges**: Color-coded indicators

### Animations

- **Fade In**: Smooth entrance animations
- **Slide Up**: Bottom-to-top transitions
- **Scale**: Hover and tap feedback
- **Pulse**: Attention-grabbing effects

## 🛠️ Available Scripts

```bash
# Development
npm run dev          # Start dev server with hot reload

# Production
npm run build        # Build for production
npm run preview      # Preview production build

# Code Quality
npm run lint         # Run ESLint
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```env
VITE_API_URL=http://localhost:8000
```

### Vite Config

The Vite config includes:
- React plugin for Fast Refresh
- Proxy to backend API
- Port configuration (3000)

### Tailwind Config

Custom theme extensions:
- Primary color palette
- Custom animations
- Keyframe definitions

## 📱 Responsive Design

The UI is fully responsive with breakpoints:
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🎯 Key Features Explained

### Agent Routing

The UI automatically displays which agent handled each message:
- 💬 **Chat Agent** - Blue badge
- 📝 **Quiz Agent** - Green badge
- 🧠 **Explanation Agent** - Purple badge

### Markdown Rendering

Messages support full Markdown:
- **Bold**, *italic*, `code`
- Lists (ordered and unordered)
- Headings (H1-H6)
- Code blocks with syntax highlighting
- Links and more

### Animations

Powered by Framer Motion:
- Message entrance animations
- Smooth transitions
- Hover effects
- Loading states

## 🚀 Deployment

### Build for Production

```bash
npm run build
```

This creates an optimized build in the `dist/` folder.

### Deploy Options

1. **Vercel** (Recommended)
   ```bash
   npm install -g vercel
   vercel
   ```

2. **Netlify**
   - Connect your Git repository
   - Build command: `npm run build`
   - Publish directory: `dist`

3. **Static Hosting**
   - Upload `dist/` folder to any static host
   - Configure environment variables

### Environment Variables for Production

Set `VITE_API_URL` to your production backend URL.

## 🎨 Customization

### Change Colors

Edit `tailwind.config.js`:

```js
theme: {
  extend: {
    colors: {
      primary: {
        // Your custom colors
      }
    }
  }
}
```

### Modify Animations

Edit `src/index.css`:

```css
@layer components {
  .your-custom-class {
    /* Your styles */
  }
}
```

### Add New Components

1. Create component in `src/components/`
2. Import in parent component
3. Use TypeScript for type safety

## 🐛 Troubleshooting

### Backend Connection Issues

**Problem**: "Error processing request"

**Solution**:
1. Ensure backend is running on port 8000
2. Check CORS settings in backend
3. Verify `.env` file has correct API URL

### Build Errors

**Problem**: TypeScript errors during build

**Solution**:
1. Run `npm install` to ensure all deps are installed
2. Check `tsconfig.json` for correct settings
3. Fix any type errors in your code

### Styling Issues

**Problem**: Tailwind classes not working

**Solution**:
1. Ensure `tailwind.config.js` includes all content paths
2. Check that `index.css` imports Tailwind directives
3. Restart dev server

## 📚 Technologies Used

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS
- **Framer Motion** - Animation library
- **Axios** - HTTP client
- **React Markdown** - Markdown rendering
- **React Syntax Highlighter** - Code highlighting
- **Lucide React** - Icon library

## 🎓 Learning Resources

- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Framer Motion Docs](https://www.framer.com/motion/)
- [Vite Guide](https://vitejs.dev/guide/)

## 🤝 Contributing

Feel free to customize and extend this frontend:
1. Add new components
2. Improve animations
3. Enhance accessibility
4. Add new features

## 📄 License

Part of the AI Teaching Assistant tutorial - free to use and modify!

---

**Built with ❤️ using React, TypeScript, and Tailwind CSS**

