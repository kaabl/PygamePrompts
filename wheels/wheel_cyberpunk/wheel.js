class Wheel {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.centerX = canvas.width / 2;
        this.centerY = canvas.height / 2;
        this.radius = Math.min(canvas.width, canvas.height) / 2 - 20;
        
        // Physics properties
        this.rotation = 0;
        this.velocity = 0;
        this.friction = 0.98;
        this.minVelocity = 0.01;
        this.isSpinning = false;
        
        // Wheel sections
        this.sections = [
            {
                name: "Rephrase & Respond",
                description: "Restate the task in your own words to confirm understanding before proceeding",
                color: "#ff00ff",
                glowColor: "#ff66ff"
            },
            {
                name: "Chain of Thought",
                description: "Explain your thought process step-by-step as you develop the answer",
                color: "#00ffff",
                glowColor: "#66ffff"
            },
            {
                name: "Chain of Knowledge",
                description: "List key facts and relevant programming concepts step-by-step as you build the answer",
                color: "#00ff00",
                glowColor: "#66ff66"
            },
            {
                name: "Reflection",
                description: "Self-review the answer for mistakes, bugs, edge cases, and missing features",
                color: "#ffff00",
                glowColor: "#ffff66"
            },
            {
                name: "Self-Consistency",
                description: "Generate alternative implementations/solutions, compare them, and choose the best approach",
                color: "#ff6600",
                glowColor: "#ff9966"
            },
            /*
            {
                name: "CLEAR",
                description: "Specify Context, preferred Language/Style, Examples, Audience, and a clear Request to guide the output.",
                color: "#8a2be2",
                glowColor: "#b388ff"
              }
            */
        ];
        
        this.sectionAngle = (2 * Math.PI) / this.sections.length;
        
        // Initialize
        this.draw();
    }
    
    spin(power = 1) {
        if (this.isSpinning) return;
        
        this.isSpinning = true;
        this.velocity = power * 0.3 + Math.random() * 0.2;
        this.animate();
    }
    
    animate() {
        if (Math.abs(this.velocity) > this.minVelocity) {
            this.rotation += this.velocity;
            this.velocity *= this.friction;
            this.draw();
            requestAnimationFrame(() => this.animate());
        } else {
            this.isSpinning = false;
            this.onSpinComplete();
        }
    }
    
    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw wheel sections
        for (let i = 0; i < this.sections.length; i++) {
            const startAngle = i * this.sectionAngle + this.rotation;
            const endAngle = (i + 1) * this.sectionAngle + this.rotation;
            
            this.drawSection(startAngle, endAngle, this.sections[i]);
        }
        
        // Draw center circle
        this.drawCenter();
        
        // Draw border
        this.drawBorder();
    }
    
    drawSection(startAngle, endAngle, section) {
        // Create gradient for glow effect
        const gradient = this.ctx.createRadialGradient(
            this.centerX, this.centerY, 0,
            this.centerX, this.centerY, this.radius
        );
        gradient.addColorStop(0, section.color);
        gradient.addColorStop(0.7, section.color);
        gradient.addColorStop(1, section.glowColor);
        
        // Draw section
        this.ctx.beginPath();
        this.ctx.moveTo(this.centerX, this.centerY);
        this.ctx.arc(this.centerX, this.centerY, this.radius, startAngle, endAngle);
        this.ctx.closePath();
        this.ctx.fillStyle = gradient;
        this.ctx.fill();
        
        // Draw section border
        this.ctx.strokeStyle = '#ffffff';
        this.ctx.lineWidth = 2;
        this.ctx.stroke();
        
        // Draw text
        this.drawSectionText(startAngle, endAngle, section.name);
    }
    
    drawSectionText(startAngle, endAngle, text) {
        const midAngle = (startAngle + endAngle) / 2;
        const textRadius = this.radius * 0.6;
        const x = this.centerX + Math.cos(midAngle) * textRadius;
        const y = this.centerY + Math.sin(midAngle) * textRadius;
        
        this.ctx.save();
        this.ctx.translate(x, y);
        this.ctx.rotate(midAngle + Math.PI / 2);
        
        this.ctx.fillStyle = '#000000';
        this.ctx.font = 'bold 14px Orbitron';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        
        // Split text into multiple lines if needed
        const words = text.split(' ');
        const lineHeight = 18;
        const lines = [];
        let currentLine = '';
        
        for (let word of words) {
            const testLine = currentLine + word + ' ';
            if (this.ctx.measureText(testLine).width > this.radius * 0.8) {
                lines.push(currentLine.trim());
                currentLine = word + ' ';
            } else {
                currentLine = testLine;
            }
        }
        lines.push(currentLine.trim());
        
        // Draw text lines
        for (let i = 0; i < lines.length; i++) {
            const yOffset = (i - (lines.length - 1) / 2) * lineHeight;
            this.ctx.fillText(lines[i], 0, yOffset);
        }
        
        this.ctx.restore();
    }
    
    drawCenter() {
        // Inner circle
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, 30, 0, 2 * Math.PI);
        this.ctx.fillStyle = '#000000';
        this.ctx.fill();
        
        // Center border
        this.ctx.strokeStyle = '#00ffff';
        this.ctx.lineWidth = 3;
        this.ctx.stroke();
        
        // Center glow
        this.ctx.shadowColor = '#00ffff';
        this.ctx.shadowBlur = 20;
        this.ctx.stroke();
        this.ctx.shadowBlur = 0;
    }
    
    drawBorder() {
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, this.radius, 0, 2 * Math.PI);
        this.ctx.strokeStyle = '#00ffff';
        this.ctx.lineWidth = 4;
        this.ctx.stroke();
        
        // Border glow
        this.ctx.shadowColor = '#00ffff';
        this.ctx.shadowBlur = 15;
        this.ctx.stroke();
        this.ctx.shadowBlur = 0;
    }
    
    getSelectedSection() {
        // Calculate which section the pointer is pointing to
        // Pointer is at the top (270 degrees)
        const pointerAngle = (270 * Math.PI) / 180;
        const normalizedRotation = (this.rotation % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI);
        const adjustedAngle = (pointerAngle - normalizedRotation + 2 * Math.PI) % (2 * Math.PI);
        
        const sectionIndex = Math.floor(adjustedAngle / this.sectionAngle);
        return this.sections[sectionIndex] || this.sections[0];
    }
    
    onSpinComplete() {
        const selectedSection = this.getSelectedSection();
        if (this.onCompleteCallback) {
            this.onCompleteCallback(selectedSection);
        }
    }
    
    setOnComplete(callback) {
        this.onCompleteCallback = callback;
    }
} 