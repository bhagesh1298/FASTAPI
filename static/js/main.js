// Main JavaScript file for FastAPI Full Stack Project

document.addEventListener('DOMContentLoaded', function() {
    console.log('FastAPI Full Stack Project loaded');
    
    // Add smooth scrolling to navigation links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add animation to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    featureCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
    
    // API testing functions (for future use)
    window.testAPI = {
        baseURL: '/api/v1',
        
        async createUser(userData) {
            try {
                const response = await fetch(`${this.baseURL}/users/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(userData)
                });
                return await response.json();
            } catch (error) {
                console.error('Error creating user:', error);
                return { error: error.message };
            }
        },
        
        async login(username, password) {
            try {
                const formData = new FormData();
                formData.append('username', username);
                formData.append('password', password);
                
                const response = await fetch(`${this.baseURL}/auth/login`, {
                    method: 'POST',
                    body: formData
                });
                return await response.json();
            } catch (error) {
                console.error('Error logging in:', error);
                return { error: error.message };
            }
        },
        
        async getUserProfile(token) {
            try {
                const response = await fetch(`${this.baseURL}/users/me`, {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });
                return await response.json();
            } catch (error) {
                console.error('Error getting user profile:', error);
                return { error: error.message };
            }
        },
        
        async createItem(itemData, token) {
            try {
                const response = await fetch(`${this.baseURL}/items/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify(itemData)
                });
                return await response.json();
            } catch (error) {
                console.error('Error creating item:', error);
                return { error: error.message };
            }
        }
    };
});
