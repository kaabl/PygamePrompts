class PromptingWheelApp {
    constructor() {
        this.canvas = document.getElementById('wheelCanvas');
        this.spinButton = document.getElementById('spinButton');
        this.resultElement = document.getElementById('result');
        this.resultTitle = document.getElementById('resultTitle');
        this.resultDescription = document.getElementById('resultDescription');
        
        this.wheel = null;
        this.soundManager = null;
        this.isSpinning = false;
        
        this.init();
    }
    
    init() {
        // Initialize wheel
        this.wheel = new Wheel(this.canvas);
        this.wheel.setOnComplete((section) => this.onSpinComplete(section));
        
        // Initialize sound manager
        this.soundManager = new SoundManager();
        
        // Set up event listeners
        this.setupEventListeners();
        
        // Handle window resize
        window.addEventListener('resize', () => this.handleResize());
        
        console.log('🎯 Cyberpunk Prompting Wheel initialized!');
    }
    
    setupEventListeners() {
        // Spin button click
        this.spinButton.addEventListener('click', () => this.spinWheel());
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.code === 'Space' && !this.isSpinning) {
                e.preventDefault();
                this.spinWheel();
            }
        });
        
        // Touch events for mobile
        this.canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            if (!this.isSpinning) {
                this.spinWheel();
            }
        });
    }
    
    spinWheel() {
        if (this.isSpinning) return;
        
        this.isSpinning = true;
        this.spinButton.disabled = true;
        this.spinButton.classList.add('glitch');
        
        // Hide previous result
        this.hideResult();
        
        // Play spin sound
        this.soundManager.playSpin();
        
        // Add spinning animation to button
        this.spinButton.querySelector('.btn-text').textContent = 'SPINNING...';
        
        // Spin the wheel with random power
        const power = 0.8 + Math.random() * 0.4;
        this.wheel.spin(power);
        
        // Re-enable button after a delay
        setTimeout(() => {
            this.spinButton.disabled = false;
            this.spinButton.classList.remove('glitch');
            this.spinButton.querySelector('.btn-text').textContent = 'SPIN THE WHEEL';
        }, 3000);
    }
    
    onSpinComplete(selectedSection) {
        this.isSpinning = false;
        
        // Play result sound
        this.soundManager.playResult();
        
        // Show result with animation
        this.showResult(selectedSection);
        
        // Add glitch effect to result
        setTimeout(() => {
            this.resultElement.classList.add('glitch');
            setTimeout(() => {
                this.resultElement.classList.remove('glitch');
            }, 300);
        }, 500);
    }
    
    showResult(section) {
        this.resultTitle.textContent = section.name;
        this.resultDescription.textContent = section.description;
        
        // Add cyberpunk styling based on section color
        this.resultElement.style.borderColor = section.color;
        this.resultElement.style.boxShadow = `0 0 30px ${section.color}40`;
        
        // Show with animation
        setTimeout(() => {
            this.resultElement.classList.remove('hidden');
            this.resultElement.classList.add('show');
        }, 100);
    }
    
    hideResult() {
        this.resultElement.classList.remove('show');
        this.resultElement.classList.add('hidden');
    }
    
    handleResize() {
        // Recalculate wheel dimensions if needed
        const rect = this.canvas.getBoundingClientRect();
        const scale = Math.min(rect.width / 600, rect.height / 600);
        
        if (scale < 1) {
            this.canvas.style.transform = `scale(${scale})`;
        } else {
            this.canvas.style.transform = 'scale(1)';
        }
    }
    
    // Public methods for external control
    setVolume(volume) {
        this.soundManager.setVolume(volume);
    }
    
    toggleSound() {
        return this.soundManager.toggle();
    }
    
    getSelectedTechnique() {
        return this.wheel.getSelectedSection();
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.promptingWheel = new PromptingWheelApp();
    
    // Add some fun console messages
    console.log('🚀 Welcome to the Cyberpunk Prompting Wheel!');
    console.log('💡 Press SPACE or click the button to spin');
    console.log('🎵 Subtle sound effects included');
    console.log('🌈 5 prompting techniques ready to be discovered');
});

// Add some fun easter eggs
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.shiftKey && e.code === 'KeyC') {
        console.log('🎮 Cheat mode activated! (Just kidding, this is already awesome)');
        document.body.style.animation = 'glitch 0.5s ease-in-out';
        setTimeout(() => {
            document.body.style.animation = '';
        }, 500);
    }
}); 