class CarnivalWheel {
    constructor() {
        this.canvas = document.getElementById('wheel');
        this.ctx = this.canvas.getContext('2d');
        this.spinBtn = document.getElementById('spinBtn');
        this.resultDiv = document.getElementById('result');
        this.resultTitle = document.getElementById('resultTitle');
        this.resultDescription = document.getElementById('resultDescription');
        
        // Wheel configuration - reordered to match visual layout
        this.segments = [
            { name: "Reflection", color: "#4ECDC4", description: "Review and improve your work with structured feedback and self-assessment." },
            { name: "Self-Consistency", color: "#45B7D1", description: "Compare alternatives and choose the best approach systematically." },
            { name: "Chain of Thought", color: "#96CEB4", description: "Plan then solve with clear step-by-step reasoning." },
            { name: "Chain of Knowledge", color: "#F39C12", description: "Map concepts to implementation with knowledge chains." },
            { name: "Rephrase & Respond", color: "#FF6B6B", description: "Clarify your goals and get precise solutions with structured responses." }
        ];
        
        this.isSpinning = false;
        this.currentRotation = 0;
        this.targetRotation = 0;
        this.spinDuration = 3000; // 3 seconds
        this.spinStartTime = 0;
        
        // Audio elements
        this.spinSound = document.getElementById('spinSound');
        this.winSound = document.getElementById('winSound');
        
        this.init();
    }
    
    init() {
        this.drawWheel();
        this.positionTextOverlays();
        this.bindEvents();
        this.setupAudio();
    }
    
    positionTextOverlays() {
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;
        const radius = Math.min(centerX, centerY) - 20;
        const textRadius = radius * 0.6; // Position text closer to center
        
        // Position each text overlay
        this.segments.forEach((segment, index) => {
            const segmentAngle = (2 * Math.PI) / this.segments.length;
            const angle = index * segmentAngle + segmentAngle / 2;
            
            const textElement = document.getElementById(`segment-${index}`);
            if (textElement) {
                const x = centerX + Math.cos(angle) * textRadius;
                const y = centerY + Math.sin(angle) * textRadius;
                
                textElement.style.left = `${x}px`;
                textElement.style.top = `${y}px`;
                // Store the base rotation for this segment
                textElement.dataset.baseRotation = `${(angle * 180 / Math.PI) + 90}`;
                textElement.style.transform = `translate(-50%, -50%) rotate(${textElement.dataset.baseRotation}deg)`;
                
                // Counter-rotate the text to keep it upright
                const textSpan = textElement.querySelector('.segment-text');
                if (textSpan) {
                    textSpan.style.transform = `rotate(${-(angle * 180 / Math.PI) - 90}deg)`;
                }
            }
        });
    }
    
    setupAudio() {
        // Set volume for carnival atmosphere
        this.spinSound.volume = 0.6;
        this.winSound.volume = 0.7;
        
        // Preload audio
        this.spinSound.load();
        this.winSound.load();
    }
    
    bindEvents() {
        this.spinBtn.addEventListener('click', () => this.spinWheel());
        this.canvas.addEventListener('click', () => this.spinWheel());
        
        // Add hover effect to technique cards
        document.querySelectorAll('.technique-card').forEach(card => {
            card.addEventListener('click', () => {
                const technique = card.dataset.technique;
                this.showResult(this.segments.find(s => 
                    s.name.toLowerCase().includes(technique.replace('-', ' '))
                ));
            });
        });
    }
    
    drawWheel() {
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;
        const radius = Math.min(centerX, centerY) - 20;
        
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw segments
        const segmentAngle = (2 * Math.PI) / this.segments.length;
        
        this.segments.forEach((segment, index) => {
            const startAngle = index * segmentAngle;
            const endAngle = startAngle + segmentAngle;
            
            // Draw segment
            this.ctx.beginPath();
            this.ctx.moveTo(centerX, centerY);
            this.ctx.arc(centerX, centerY, radius, startAngle, endAngle);
            this.ctx.closePath();
            this.ctx.fillStyle = segment.color;
            this.ctx.fill();
            
            // Add segment border
            this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
            this.ctx.lineWidth = 3;
            this.ctx.stroke();
            
            // Text will be rendered as HTML overlays instead of canvas text
        });
        
        // Draw center circle
        this.ctx.beginPath();
        this.ctx.arc(centerX, centerY, 15, 0, 2 * Math.PI);
        this.ctx.fillStyle = '#2C3E50';
        this.ctx.fill();
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        this.ctx.lineWidth = 3;
        this.ctx.stroke();
        
        // Add carnival decorations
        this.drawDecorations(centerX, centerY, radius);
    }
    
    drawDecorations(centerX, centerY, radius) {
        // Draw sparkles around the wheel
        for (let i = 0; i < 12; i++) {
            const angle = (i * Math.PI * 2) / 12;
            const x = centerX + Math.cos(angle) * (radius + 15);
            const y = centerY + Math.sin(angle) * (radius + 15);
            
            this.ctx.beginPath();
            this.ctx.arc(x, y, 3, 0, 2 * Math.PI);
            this.ctx.fillStyle = `hsl(${i * 30}, 70%, 60%)`;
            this.ctx.fill();
        }
        
        // Draw inner ring
        this.ctx.beginPath();
        this.ctx.arc(centerX, centerY, radius - 10, 0, 2 * Math.PI);
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        this.ctx.lineWidth = 1;
        this.ctx.stroke();
    }
    
    spinWheel() {
        if (this.isSpinning) return;
        
        this.isSpinning = true;
        this.spinBtn.disabled = true;
        this.hideResult();
        
        // Play carnival sound
        this.playSpinSound();
        
        // Calculate random target rotation
        const extraSpins = 5 + Math.random() * 5; // 5-10 full rotations
        const randomSegment = Math.floor(Math.random() * this.segments.length);
        const segmentAngle = (2 * Math.PI) / this.segments.length;
        const targetSegmentAngle = randomSegment * segmentAngle + segmentAngle / 2;
        
        this.targetRotation = this.currentRotation + (extraSpins * 2 * Math.PI) + targetSegmentAngle;
        this.spinStartTime = Date.now();
        
        // Start spinning animation
        this.animate();
    }
    
    animate() {
        const elapsed = Date.now() - this.spinStartTime;
        const progress = Math.min(elapsed / this.spinDuration, 1);
        
        // Easing function for realistic spinning
        const easeOut = 1 - Math.pow(1 - progress, 3);
        
        this.currentRotation = this.currentRotation + (this.targetRotation - this.currentRotation) * easeOut;
        
        // Apply rotation to canvas
        this.canvas.style.transform = `rotate(${this.currentRotation}rad)`;
        
        // Apply same rotation to all text overlays so they move with the wheel
        this.segments.forEach((segment, index) => {
            const textElement = document.getElementById(`segment-${index}`);
            if (textElement) {
                const baseRotation = textElement.dataset.baseRotation || '0';
                const wheelRotation = this.currentRotation * 180 / Math.PI;
                textElement.style.transform = `translate(-50%, -50%) rotate(${baseRotation}deg) rotate(${wheelRotation}deg)`;
            }
        });
        
        if (progress < 1) {
            requestAnimationFrame(() => this.animate());
        } else {
            this.finishSpin();
        }
    }
    
    finishSpin() {
        this.isSpinning = false;
        this.spinBtn.disabled = false;
        
        // Play win sound
        this.playWinSound();
        
        // Determine which segment the pointer is pointing to
        const normalizedRotation = this.currentRotation % (2 * Math.PI);
        const segmentAngle = (2 * Math.PI) / this.segments.length;
        const pointerAngle = (2 * Math.PI - normalizedRotation) % (2 * Math.PI);
        const segmentIndex = Math.floor(pointerAngle / segmentAngle);
        
        // Show result
        setTimeout(() => {
            this.showResult(this.segments[segmentIndex]);
        }, 500);
    }
    
    playSpinSound() {
        this.spinSound.currentTime = 0;
        this.spinSound.play().catch(e => console.log('Audio play failed:', e));
    }
    
    playWinSound() {
        this.winSound.currentTime = 0;
        this.winSound.play().catch(e => console.log('Audio play failed:', e));
    }
    
    showResult(segment) {
        this.resultTitle.textContent = segment.name;
        this.resultDescription.textContent = segment.description;
        this.resultDiv.classList.remove('hidden');
        
        // Add carnival celebration effect
        this.celebrate();
    }
    
    hideResult() {
        this.resultDiv.classList.add('hidden');
    }
    
    celebrate() {
        // Add confetti effect
        this.createConfetti();
        
        // Highlight the corresponding technique card
        const techniqueName = segment.name.toLowerCase().replace(/\s+/g, '-');
        document.querySelectorAll('.technique-card').forEach(card => {
            if (card.dataset.technique === techniqueName.replace(/\s+/g, '-')) {
                card.style.transform = 'scale(1.1)';
                card.style.borderColor = '#feca57';
                setTimeout(() => {
                    card.style.transform = '';
                    card.style.borderColor = '';
                }, 2000);
            }
        });
    }
    
    createConfetti() {
        const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#FDCB6E'];
        
        for (let i = 0; i < 50; i++) {
            setTimeout(() => {
                const confetti = document.createElement('div');
                confetti.style.position = 'fixed';
                confetti.style.left = Math.random() * 100 + 'vw';
                confetti.style.top = '-10px';
                confetti.style.width = '10px';
                confetti.style.height = '10px';
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.borderRadius = '50%';
                confetti.style.pointerEvents = 'none';
                confetti.style.zIndex = '1000';
                
                document.body.appendChild(confetti);
                
                // Animate confetti falling
                const animation = confetti.animate([
                    { transform: 'translateY(0px) rotate(0deg)', opacity: 1 },
                    { transform: `translateY(${window.innerHeight + 100}px) rotate(${Math.random() * 360}deg)`, opacity: 0 }
                ], {
                    duration: 3000 + Math.random() * 2000,
                    easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
                });
                
                animation.onfinish = () => confetti.remove();
            }, i * 50);
        }
    }
}

// Initialize the wheel when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new CarnivalWheel();
});

// Add some carnival atmosphere with background effects
document.addEventListener('DOMContentLoaded', () => {
    // Create floating bubbles
    for (let i = 0; i < 20; i++) {
        createBubble();
    }
});

function createBubble() {
    const bubble = document.createElement('div');
    bubble.style.position = 'fixed';
    bubble.style.width = Math.random() * 20 + 10 + 'px';
    bubble.style.height = bubble.style.width;
    bubble.style.backgroundColor = `hsla(${Math.random() * 360}, 70%, 80%, 0.1)`;
    bubble.style.borderRadius = '50%';
    bubble.style.left = Math.random() * 100 + 'vw';
    bubble.style.top = '100vh';
    bubble.style.pointerEvents = 'none';
    bubble.style.zIndex = '-1';
    
    document.body.appendChild(bubble);
    
    // Animate bubble floating up
    const animation = bubble.animate([
        { transform: 'translateY(0px)', opacity: 0.1 },
        { transform: 'translateY(-100vh)', opacity: 0.3 }
    ], {
        duration: 10000 + Math.random() * 10000,
        easing: 'linear'
    });
    
    animation.onfinish = () => {
        bubble.remove();
        setTimeout(createBubble, Math.random() * 5000);
    };
}
