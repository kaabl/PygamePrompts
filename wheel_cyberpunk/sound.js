class SoundManager {
    constructor() {
        this.audioContext = null;
        this.sounds = {};
        this.isEnabled = true;
        this.volume = 0.3;
        
        this.init();
    }
    
    init() {
        try {
            // Create audio context
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            // Pre-create sounds
            this.createSpinSound();
            this.createResultSound();
            this.createClickSound();
            
        } catch (error) {
            console.log('Audio not supported, running without sound');
            this.isEnabled = false;
        }
    }
    
    createSpinSound() {
        if (!this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(200, this.audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(50, this.audioContext.currentTime + 2);
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(this.volume * 0.5, this.audioContext.currentTime + 0.1);
        gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioContext.currentTime + 2);
        
        this.sounds.spin = { oscillator, gainNode };
    }
    
    createResultSound() {
        if (!this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.type = 'square';
        oscillator.frequency.setValueAtTime(400, this.audioContext.currentTime);
        oscillator.frequency.setValueAtTime(600, this.audioContext.currentTime + 0.1);
        oscillator.frequency.setValueAtTime(800, this.audioContext.currentTime + 0.2);
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(this.volume * 0.3, this.audioContext.currentTime + 0.05);
        gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioContext.currentTime + 0.5);
        
        this.sounds.result = { oscillator, gainNode };
    }
    
    createClickSound() {
        if (!this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(800, this.audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(400, this.audioContext.currentTime + 0.1);
        
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(this.volume * 0.2, this.audioContext.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.001, this.audioContext.currentTime + 0.1);
        
        this.sounds.click = { oscillator, gainNode };
    }
    
    playSpin() {
        if (!this.isEnabled || !this.audioContext) return;
        
        try {
            this.audioContext.resume();
            this.createSpinSound();
            this.sounds.spin.oscillator.start();
            this.sounds.spin.oscillator.stop(this.audioContext.currentTime + 2);
        } catch (error) {
            console.log('Error playing spin sound:', error);
        }
    }
    
    playResult() {
        if (!this.isEnabled || !this.audioContext) return;
        
        try {
            this.audioContext.resume();
            this.createResultSound();
            this.sounds.result.oscillator.start();
            this.sounds.result.oscillator.stop(this.audioContext.currentTime + 0.5);
        } catch (error) {
            console.log('Error playing result sound:', error);
        }
    }
    
    playClick() {
        if (!this.isEnabled || !this.audioContext) return;
        
        try {
            this.audioContext.resume();
            this.createClickSound();
            this.sounds.click.oscillator.start();
            this.sounds.click.oscillator.stop(this.audioContext.currentTime + 0.1);
        } catch (error) {
            console.log('Error playing click sound:', error);
        }
    }
    
    setVolume(volume) {
        this.volume = Math.max(0, Math.min(1, volume));
    }
    
    toggle() {
        this.isEnabled = !this.isEnabled;
        return this.isEnabled;
    }
    
    enable() {
        this.isEnabled = true;
    }
    
    disable() {
        this.isEnabled = false;
    }
} 