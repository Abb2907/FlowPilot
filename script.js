// Demo Tab Switching
document.addEventListener('DOMContentLoaded', function() {
    // Tab functionality
    const tabButtons = document.querySelectorAll('.tab-btn');
    const demoPanels = document.querySelectorAll('.demo-panel');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');
            
            // Remove active class from all tabs and panels
            tabButtons.forEach(btn => btn.classList.remove('active'));
            demoPanels.forEach(panel => panel.classList.remove('active'));
            
            // Add active class to clicked tab and corresponding panel
            button.classList.add('active');
            document.getElementById(`${targetTab}-panel`).classList.add('active');
        });
    });
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const navHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = target.offsetTop - navHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.8)';
            navbar.style.boxShadow = 'none';
        }
    });
    
    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe feature cards
    document.querySelectorAll('.feature-card, .step, .integration-card, .pricing-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Terminal typing animation
    const terminalLines = document.querySelectorAll('.terminal-line');
    let delay = 0;
    
    terminalLines.forEach((line, index) => {
        line.style.opacity = '0';
        setTimeout(() => {
            line.style.transition = 'opacity 0.3s ease';
            line.style.opacity = '1';
        }, delay);
        delay += 300;
    });
    
    // Stats counter animation
    const animateCounter = (element, target, duration = 2000) => {
        const start = 0;
        const increment = target / (duration / 16);
        let current = start;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current);
            }
        }, 16);
    };
    
    // Observe stats section
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statValues = entry.target.querySelectorAll('.stat-value');
                statValues.forEach(stat => {
                    const text = stat.textContent;
                    if (text.includes('%')) {
                        const value = parseInt(text);
                        stat.textContent = '0%';
                        animateCounter(stat, value);
                        stat.textContent += '%';
                    } else if (text.includes('x')) {
                        stat.textContent = '0x';
                        setTimeout(() => {
                            stat.textContent = text;
                        }, 1000);
                    }
                });
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        statsObserver.observe(heroStats);
    }
    
    // Button click effects
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function(e) {
            // Create ripple effect
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.style.position = 'absolute';
            ripple.style.borderRadius = '50%';
            ripple.style.background = 'rgba(255, 255, 255, 0.5)';
            ripple.style.transform = 'scale(0)';
            ripple.style.animation = 'ripple 0.6s ease-out';
            ripple.style.pointerEvents = 'none';
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
    });
    
    // Add ripple animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Pricing card hover effect
    document.querySelectorAll('.pricing-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.borderColor = 'var(--primary)';
        });
        
        card.addEventListener('mouseleave', function() {
            if (!this.classList.contains('featured')) {
                this.style.borderColor = 'var(--border)';
            }
        });
    });
    
    // Code block syntax highlighting (simple)
    document.querySelectorAll('.code-block code').forEach(block => {
        let html = block.innerHTML;
        
        // Highlight comments
        html = html.replace(/(#.*$)/gm, '<span style="color: #6b7280;">$1</span>');
        
        // Highlight strings
        html = html.replace(/(".*?"|'.*?')/g, '<span style="color: #34d399;">$1</span>');
        
        // Highlight keywords
        const keywords = ['def', 'class', 'import', 'from', 'return', 'if', 'else', 'for', 'while', 'async', 'await', 'try', 'except'];
        keywords.forEach(keyword => {
            const regex = new RegExp(`\\b${keyword}\\b`, 'g');
            html = html.replace(regex, `<span style="color: #c084fc;">${keyword}</span>`);
        });
        
        // Highlight functions
        html = html.replace(/\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g, '<span style="color: #60a5fa;">$1</span>(');
        
        block.innerHTML = html;
    });
    
    // Mobile menu toggle (if needed)
    const createMobileMenu = () => {
        if (window.innerWidth <= 768) {
            const navLinks = document.querySelector('.nav-links');
            const navActions = document.querySelector('.nav-actions');
            
            if (navLinks && !document.querySelector('.mobile-menu-btn')) {
                const menuBtn = document.createElement('button');
                menuBtn.className = 'mobile-menu-btn';
                menuBtn.innerHTML = '☰';
                menuBtn.style.cssText = `
                    display: block;
                    background: none;
                    border: none;
                    font-size: 1.5rem;
                    cursor: pointer;
                    color: var(--text-primary);
                `;
                
                document.querySelector('.nav-content').appendChild(menuBtn);
                
                menuBtn.addEventListener('click', () => {
                    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
                    navLinks.style.flexDirection = 'column';
                    navLinks.style.position = 'absolute';
                    navLinks.style.top = '100%';
                    navLinks.style.left = '0';
                    navLinks.style.right = '0';
                    navLinks.style.background = 'white';
                    navLinks.style.padding = '1rem';
                    navLinks.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
                });
            }
        }
    };
    
    createMobileMenu();
    window.addEventListener('resize', createMobileMenu);
    
    // Add loading animation
    window.addEventListener('load', () => {
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.3s ease';
        setTimeout(() => {
            document.body.style.opacity = '1';
        }, 100);
    });
    
    // Console easter egg
    console.log('%c🚀 FlowPilot', 'font-size: 24px; font-weight: bold; color: #6366f1;');
    console.log('%cInterested in how this works? Check out our documentation!', 'font-size: 14px; color: #64748b;');
    console.log('%chttps://github.com/flowpilot', 'font-size: 12px; color: #6366f1;');
});

// Made with Bob
