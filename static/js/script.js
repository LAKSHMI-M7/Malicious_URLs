document.addEventListener('DOMContentLoaded', () => {
    // Tab Switching Logic
    const tabs = document.querySelectorAll('.nav-tab');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-tab');
            
            // Update tabs
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Update content
            contents.forEach(c => {
                c.classList.remove('active');
                if (c.id === target) {
                    c.classList.add('active');
                }
            });
        });
    });

    // URL Checker Logic
    const urlInput = document.getElementById('url-input');
    const checkBtn = document.getElementById('check-btn');
    const btnText = checkBtn.querySelector('.btn-text');
    const btnIcon = checkBtn.querySelector('.btn-icon');
    const loader = checkBtn.querySelector('.loader-spinner');
    const validationError = document.getElementById('validation-error');
    const resultSection = document.getElementById('result-section');
    const resultCard = document.getElementById('result-card');
    const predictionLabel = document.getElementById('prediction-label');
    const riskBadge = document.getElementById('risk-badge');
    const confidenceFill = document.getElementById('confidence-fill');
    const confidenceText = document.getElementById('confidence-text');
    const statusIcon = document.getElementById('status-icon');

    const validateURL = (url) => {
        // Simple URL validation regex
        if (!url) return false;
        if (url.length < 3) return false;
        return true;
    };

    const updateUIState = (isLoading) => {
        if (isLoading) {
            checkBtn.disabled = true;
            btnText.style.opacity = '0';
            btnIcon.classList.add('hidden');
            loader.classList.remove('hidden');
            validationError.classList.add('hidden');
        } else {
            checkBtn.disabled = false;
            btnText.style.opacity = '1';
            btnIcon.classList.remove('hidden');
            loader.classList.add('hidden');
        }
    };

    const showResult = (data) => {
        const { label, risk, confidence, icon } = data;
        
        resultSection.classList.remove('hidden');
        predictionLabel.textContent = label;
        riskBadge.textContent = risk + ' Risk';
        confidenceText.textContent = confidence + '%';
        confidenceFill.style.width = confidence + '%';
        
        // Remove old classes
        riskBadge.className = 'badge';
        resultCard.style.borderColor = 'var(--glass-border)';
        
        // Set Theme based on prediction
        let accentColor = 'var(--accent-blue)';
        if (label === 'Safe (Benign)') {
            riskBadge.classList.add('benign-badge');
            riskBadge.style.backgroundColor = 'rgba(74, 222, 128, 0.2)';
            riskBadge.style.color = 'var(--accent-green)';
            accentColor = 'var(--accent-green)';
            statusIcon.setAttribute('data-lucide', 'shield-check');
        } else if (label === 'Defacement') {
            riskBadge.style.backgroundColor = 'rgba(251, 191, 36, 0.2)';
            riskBadge.style.color = 'var(--accent-yellow)';
            accentColor = 'var(--accent-yellow)';
            statusIcon.setAttribute('data-lucide', 'alert-triangle');
        } else {
            riskBadge.style.backgroundColor = 'rgba(248, 113, 113, 0.2)';
            riskBadge.style.color = 'var(--accent-red)';
            accentColor = 'var(--accent-red)';
            statusIcon.setAttribute('data-lucide', 'alert-octagon');
        }

        // Apply accent colors
        confidenceFill.style.backgroundColor = accentColor;
        confidenceText.style.color = accentColor;
        statusIcon.style.color = accentColor;
        
        // Finalize icons
        lucide.createIcons();
    };

    checkBtn.addEventListener('click', async () => {
        const url = urlInput.value.trim();
        
        if (!validateURL(url)) {
            validationError.classList.remove('hidden');
            return;
        }

        updateUIState(true);
        resultSection.classList.add('hidden');

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url })
            });

            if (!response.ok) throw new Error('Prediction failed');
            
            const data = await response.json();
            
            // Add a small delay for better UX
            setTimeout(() => {
                updateUIState(false);
                showResult(data);
            }, 600);

        } catch (error) {
            console.error('Error:', error);
            updateUIState(false);
            alert('An error occurred while analyzing the URL. Please try again.');
        }
    });

    // Enter key support
    urlInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') checkBtn.click();
    });
});
