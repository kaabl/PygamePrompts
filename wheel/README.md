# 🎪 Carnival Prompting Wheel 🎪

A colorful, interactive wheel game that helps workshop participants learn and practice different AI prompting techniques through a fun carnival experience!

## 🚀 Quick Start

1. **Open the game**: Simply open `index.html` in any modern web browser
2. **Spin the wheel**: Click the colorful "SPIN THE WHEEL!" button or click directly on the wheel
3. **Discover techniques**: Watch the wheel spin with carnival sounds and see which prompting technique you land on
4. **Learn more**: Click on any technique card below the wheel to see detailed information

## 🎯 Features

- **Colorful Wheel**: 5 vibrant segments representing different prompting techniques
- **Carnival Sounds**: Bell ringing during spin, celebration sound when landing
- **Smooth Animation**: Realistic spinning physics with easing
- **Interactive Cards**: Click technique cards to learn more
- **Confetti Celebration**: Festive effects when the wheel stops
- **Responsive Design**: Works on desktop and mobile devices
- **Floating Bubbles**: Ambient carnival atmosphere

## 🎨 Prompting Techniques

The wheel includes these 5 core prompting techniques:

### 🔄 Rephrase & Respond
- **Purpose**: Clarify goals and get precise solutions
- **Best for**: Project kickoffs, complex requests, alignment
- **Workshop use**: Start each major feature with this technique

### 🤔 Reflection
- **Purpose**: Review and improve with structured feedback
- **Best for**: Code reviews, quality improvements, post-implementation
- **Workshop use**: After each development stage

### ⚖️ Self-Consistency
- **Purpose**: Compare alternatives and choose the best approach
- **Best for**: Design decisions, multiple solution paths
- **Workshop use**: When there are architectural choices to make

### 🧠 Chain of Thought
- **Purpose**: Plan then solve with clear step-by-step reasoning
- **Best for**: Complex features, breaking down tasks
- **Workshop use**: Implementing focused feature slices

### 📚 Chain of Knowledge
- **Purpose**: Map concepts to implementation with knowledge chains
- **Best for**: Learning new APIs, understanding dependencies
- **Workshop use**: When introducing new technologies or concepts

## 🎮 How to Use in Workshops

### Setup (5 minutes)
1. Open the carnival wheel in a browser
2. Explain the 5 prompting techniques briefly
3. Demonstrate spinning the wheel once

### Workshop Flow
1. **Kickoff**: Use "Rephrase & Respond" to start the Snake game project
2. **Development**: Spin for each major feature (movement, food, collisions)
3. **Quality**: Use "Reflection" after each stage
4. **Decisions**: Use "Self-Consistency" for design choices
5. **Complex Features**: Use "Chain of Thought" for detailed implementations
6. **Learning**: Use "Chain of Knowledge" for new concepts

### Interactive Elements
- **Random Selection**: Let participants spin to determine which technique to use
- **Technique Cards**: Click cards to show detailed explanations
- **Group Decisions**: Spin the wheel to choose approach for team challenges

## 🛠️ Technical Details

- **Pure HTML/CSS/JavaScript**: No external dependencies
- **Canvas-based Wheel**: Smooth graphics and animations
- **Audio Integration**: Carnival sound effects
- **Responsive Design**: Mobile-friendly interface
- **Modern CSS**: Animations, gradients, and effects

## 🎨 Customization

### Adding New Techniques
Edit the `segments` array in `script.js`:
```javascript
this.segments = [
    { name: "New Technique", color: "#HEXCODE", description: "Description here" },
    // ... existing techniques
];
```

### Changing Colors
Modify the color values in the segments array or CSS variables

### Adjusting Animation
- **Spin Duration**: Change `spinDuration` in the constructor
- **Rotation Speed**: Modify the easing function in `animate()`
- **Confetti Amount**: Adjust the loop count in `createConfetti()`

## 🌟 Workshop Tips

1. **Keep it Fun**: The carnival theme makes learning engaging
2. **Random Selection**: Let the wheel decide which technique to practice
3. **Group Participation**: Have multiple people spin for different features
4. **Technique Cards**: Use the detailed explanations for deeper learning
5. **Celebration**: The confetti effect creates memorable moments

## 🔧 Troubleshooting

- **Audio not working**: Check browser autoplay settings
- **Wheel not spinning**: Ensure JavaScript is enabled
- **Mobile issues**: Test on different screen sizes
- **Performance**: Reduce confetti count on slower devices

## 📚 Learning Resources

- **Prompting Fundamentals**: Start with "Rephrase & Respond"
- **Quality Assurance**: Practice "Reflection" regularly
- **Decision Making**: Use "Self-Consistency" for choices
- **Complex Tasks**: Apply "Chain of Thought" systematically
- **New Concepts**: Leverage "Chain of Knowledge" for learning

---

**Happy Prompting! 🎪✨**

*Spin the wheel and discover the power of structured AI prompting techniques!*
