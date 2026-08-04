// Force Scroll Restoration to Manual to prevent auto-scrolling glitches on refresh
if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}
window.scrollTo(0, 0);

// CineIntelligence™ Advanced JS Animation & Frontend Component Engine
let probChart = null;

document.addEventListener('DOMContentLoaded', () => {
    // Scroll to top cleanly
    window.scrollTo(0, 0);

    // Initialize AOS Scroll Animations cleanly
    if (typeof AOS !== 'undefined') {
        AOS.init({ 
            duration: 800, 
            once: true,
            offset: 50,
            startEvent: 'DOMContentLoaded'
        });
    }

    const form = document.getElementById('prediction-form');
    const resultsContainer = document.getElementById('results-container');

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Collect form values
            const title = document.getElementById('title').value;
            const primary_genre = document.getElementById('primary_genre').value;
            const language = document.getElementById('language').value;
            const runtime_minutes = parseFloat(document.getElementById('runtime_minutes').value);
            
            const director_name = document.getElementById('director_name').value;
            const production_house = document.getElementById('production_house').value;
            const lead_actor = document.getElementById('lead_actor').value;
            const lead_actress = document.getElementById('lead_actress').value;
            const music_director = document.getElementById('music_director').value;
            
            const currency = document.getElementById('currency').value;
            const budget_unit = document.getElementById('budget_unit').value;
            const production_budget_val = parseFloat(document.getElementById('production_budget_val').value);
            const marketing_budget_val = parseFloat(document.getElementById('marketing_budget_val').value);
            const sentiment = document.getElementById('sentiment').value;

            // Collect multi-select checkboxes
            const content_themes = Array.from(document.querySelectorAll('input[name="content_themes"]:checked')).map(cb => cb.value);
            const popularity_tags = Array.from(document.querySelectorAll('input[name="popularity_tags"]:checked')).map(cb => cb.value);

            const payload = {
                title,
                primary_genre,
                language,
                country: 'India',
                runtime_minutes,
                director_name,
                production_house,
                lead_actor,
                lead_actress,
                co_actors: 'Vijay Sethupathi, Fahadh Faasil',
                music_director,
                currency,
                budget_unit,
                production_budget_val,
                marketing_budget_val,
                sentiment,
                content_themes,
                popularity_tags,
                release_year: 2025,
                content_rating: 'UA'
            };

            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            
            // GSAP Loading Pulse Animation on Button
            if (typeof gsap !== 'undefined') {
                gsap.to(submitBtn, { scale: 0.98, duration: 0.1, yoyo: true, repeat: 1 });
            }
            
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Running Machine Learning Inference...';
            submitBtn.disabled = true;

            try {
                const response = await fetch('/api/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const resJson = await response.json();
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;

                if (resJson.status === 'success') {
                    const data = resJson.data;
                    const cat = data.predicted_category;
                    const confidence = data.confidence;
                    const probs = data.probabilities || { High: 0.98, Medium: 0.015, Low: 0.005 };
                    const recs = data.recommendations;
                    const rep = data.reputation_indices || {};

                    // Update UI Card Status
                    const cardBox = document.getElementById('result-card-box');
                    const badge = document.getElementById('res-badge');
                    const heading = document.getElementById('res-heading');
                    
                    cardBox.className = `result-card ${cat.toLowerCase()}`;
                    badge.className = `badge ${cat.toLowerCase()}`;
                    badge.innerText = cat.toUpperCase();

                    const iconClass = cat === 'High' ? 'fa-circle-check' : (cat === 'Medium' ? 'fa-triangle-exclamation' : 'fa-circle-xmark');
                    heading.innerHTML = `<i class="fa-solid ${iconClass}"></i> ${cat} Quality`;

                    document.getElementById('res-confidence').innerText = `${confidence}%`;
                    document.getElementById('res-action').innerText = recs.action_badge;

                    // Update Reputation Metrics with Animated CountUp
                    animateNumber('idx-dir', parseFloat(rep.director_index || 7.5));
                    animateNumber('idx-actor', parseFloat(rep.actor_index || 7.0));
                    animateNumber('idx-music', parseFloat(rep.music_director_index || 7.0));
                    animateNumber('idx-banner', parseFloat(rep.production_house_index || 7.5));

                    // Update Strategic Content Recommendations
                    document.getElementById('strat-tier').innerText = recs.acquisition_tier;
                    document.getElementById('strat-mkt').innerText = recs.marketing_strategy;
                    document.getElementById('strat-dist').innerText = recs.platform_positioning;

                    // Render Chart.js Probability Doughnut Chart
                    renderProbabilityChart([probs.High * 100, probs.Medium * 100, probs.Low * 100]);

                    // Trigger Confetti Celebration if High Quality
                    if (cat === 'High' && typeof confetti !== 'undefined') {
                        confetti({
                            particleCount: 100,
                            spread: 70,
                            origin: { y: 0.6 }
                        });
                    }

                    // Reveal Results with Smooth GSAP Animation
                    resultsContainer.style.display = 'block';
                    if (typeof gsap !== 'undefined') {
                        gsap.fromTo(resultsContainer, 
                            { opacity: 0, y: 30 }, 
                            { opacity: 1, y: 0, duration: 0.6, ease: 'power2.out' }
                        );
                    }

                    // Precise Scroll Alignment below Fixed Navbar
                    const navHeight = 90;
                    const targetY = resultsContainer.getBoundingClientRect().top + window.pageYOffset - navHeight;
                    window.scrollTo({ top: targetY, behavior: 'smooth' });

                } else {
                    alert('Prediction Error: ' + resJson.message);
                }
            } catch (err) {
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
                alert('Network / API Error: ' + err.message);
            }
        });
    }
});

// Helper Function: Chart.js Doughnut Chart Renderer
function renderProbabilityChart(probData) {
    const ctx = document.getElementById('probChart');
    if (!ctx) return;

    if (probChart) {
        probChart.destroy();
    }

    probChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['High (≥ 7.5)', 'Medium (5.5 - 7.4)', 'Low (< 5.5)'],
            datasets: [{
                data: probData,
                backgroundColor: ['#16a34a', '#d97706', '#dc2626'],
                borderWidth: 2,
                borderColor: '#ffffff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                animateScale: true,
                animateRotate: true,
                duration: 1200
            },
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        boxWidth: 12,
                        font: { family: 'Plus Jakarta Sans', weight: '600', size: 11 }
                    }
                }
            }
        }
    });
}

// Helper Function: Number CountUp Animation
function animateNumber(elementId, targetVal) {
    const el = document.getElementById(elementId);
    if (!el) return;

    let start = 0;
    const duration = 1000;
    const stepTime = 20;
    const steps = duration / stepTime;
    const increment = targetVal / steps;

    const timer = setInterval(() => {
        start += increment;
        if (start >= targetVal) {
            el.innerText = targetVal.toFixed(1);
            clearInterval(timer);
        } else {
            el.innerText = start.toFixed(1);
        }
    }, stepTime);
}
