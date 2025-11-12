/**
 * Endpoint.US Animations JavaScript
 * Handles scroll animations, fade-ins, and interactive effects
 */

(function() {
    'use strict';

    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {

        // ============================================
        // INTERSECTION OBSERVER FOR SCROLL ANIMATIONS
        // ============================================
        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -100px 0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');

                    // Optionally unobserve after animation
                    // observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observe all elements with fade-in-on-scroll class
        const fadeElements = document.querySelectorAll('.fade-in-on-scroll');
        fadeElements.forEach(function(el) {
            observer.observe(el);
        });

        // Auto-add fade-in class to common elements
        const autoFadeElements = document.querySelectorAll('.card, .service-card, .industry-card, .stat, .process-step');
        autoFadeElements.forEach(function(el, index) {
            // Stagger animation delays
            el.style.transitionDelay = (index * 0.05) + 's';
            el.classList.add('fade-in-on-scroll');
            observer.observe(el);
        });

        // ============================================
        // BACK TO TOP BUTTON
        // ============================================
        const backToTopButton = document.querySelector('.back-to-top');

        if (backToTopButton) {
            // Show/hide button based on scroll position
            window.addEventListener('scroll', function() {
                if (window.pageYOffset > 300) {
                    backToTopButton.classList.add('visible');
                } else {
                    backToTopButton.classList.remove('visible');
                }
            });

            // Scroll to top on click
            backToTopButton.addEventListener('click', function() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        }

        // ============================================
        // FAQ ACCORDION
        // ============================================
        const faqQuestions = document.querySelectorAll('.faq-question');

        faqQuestions.forEach(function(question) {
            question.addEventListener('click', function() {
                const answer = this.nextElementSibling;

                // Toggle active class
                this.classList.toggle('active');
                answer.classList.toggle('active');

                // Update aria-expanded
                const isExpanded = this.classList.contains('active');
                this.setAttribute('aria-expanded', isExpanded);

                // Close other FAQs (optional - comment out for multi-open)
                /*
                faqQuestions.forEach(function(otherQuestion) {
                    if (otherQuestion !== question && otherQuestion.classList.contains('active')) {
                        otherQuestion.classList.remove('active');
                        otherQuestion.nextElementSibling.classList.remove('active');
                        otherQuestion.setAttribute('aria-expanded', 'false');
                    }
                });
                */
            });

            // Keyboard accessibility
            question.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    this.click();
                }
            });
        });

        // ============================================
        // ANIMATED COUNTERS FOR STATS
        // ============================================
        const statValues = document.querySelectorAll('.stat-value');

        const animateCounter = function(element) {
            const target = parseInt(element.getAttribute('data-target')) || parseInt(element.textContent);
            const duration = 2000; // 2 seconds
            const increment = target / (duration / 16); // 60fps
            let current = 0;

            // Store original text for non-numeric content
            const originalText = element.textContent;
            const hasNonNumeric = /[^\d]/.test(originalText);

            const updateCounter = function() {
                current += increment;

                if (current < target) {
                    if (hasNonNumeric) {
                        // Extract and update just the number part
                        element.textContent = originalText.replace(/\d+/, Math.floor(current));
                    } else {
                        element.textContent = Math.floor(current);
                    }
                    requestAnimationFrame(updateCounter);
                } else {
                    element.textContent = originalText;
                }
            };

            updateCounter();
        };

        // Observe stat elements
        const statObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    animateCounter(entry.target);
                    entry.target.classList.add('counted');
                    statObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        statValues.forEach(function(stat) {
            statObserver.observe(stat);
        });

        // ============================================
        // LAZY LOADING IMAGES
        // ============================================
        const lazyImages = document.querySelectorAll('img[data-src]');

        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;

                    // Optional: handle srcset
                    if (img.dataset.srcset) {
                        img.srcset = img.dataset.srcset;
                    }

                    img.addEventListener('load', function() {
                        img.classList.add('loaded');
                        img.removeAttribute('data-src');
                    });

                    imageObserver.unobserve(img);
                }
            });
        }, { rootMargin: '50px' });

        lazyImages.forEach(function(img) {
            imageObserver.observe(img);
        });

        // ============================================
        // PARALLAX EFFECT (Desktop only)
        // ============================================
        if (window.innerWidth >= 1024) {
            const parallaxElements = document.querySelectorAll('.parallax-section');

            window.addEventListener('scroll', function() {
                const scrolled = window.pageYOffset;

                parallaxElements.forEach(function(el) {
                    const speed = el.dataset.speed || 0.5;
                    const offset = scrolled * speed;
                    el.style.transform = 'translateY(' + offset + 'px)';
                });
            });
        }

        // ============================================
        // CARD HOVER TILT EFFECT (Desktop only)
        // ============================================
        if (window.innerWidth >= 1024 && window.matchMedia('(hover: hover)').matches) {
            const tiltCards = document.querySelectorAll('.card-tilt');

            tiltCards.forEach(function(card) {
                card.addEventListener('mousemove', function(e) {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;

                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;

                    const rotateX = (y - centerY) / 20;
                    const rotateY = (centerX - x) / 20;

                    card.style.transform = 'perspective(1000px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) scale3d(1.02, 1.02, 1.02)';
                });

                card.addEventListener('mouseleave', function() {
                    card.style.transform = '';
                });
            });
        }

        // ============================================
        // PROGRESS BARS ANIMATION
        // ============================================
        const progressBars = document.querySelectorAll('.progress-bar');

        const progressObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const bar = entry.target;
                    const progress = bar.dataset.progress || 0;

                    setTimeout(function() {
                        bar.style.width = progress + '%';
                    }, 100);

                    progressObserver.unobserve(bar);
                }
            });
        }, { threshold: 0.5 });

        progressBars.forEach(function(bar) {
            progressObserver.observe(bar);
        });

        // ============================================
        // TYPING EFFECT (Optional)
        // ============================================
        const typingElements = document.querySelectorAll('[data-typing]');

        typingElements.forEach(function(el) {
            const text = el.textContent;
            const speed = parseInt(el.dataset.typingSpeed) || 50;

            el.textContent = '';
            el.style.visibility = 'visible';

            let i = 0;
            const typeWriter = function() {
                if (i < text.length) {
                    el.textContent += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, speed);
                }
            };

            // Start typing when element is in view
            const typingObserver = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        typeWriter();
                        typingObserver.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.5 });

            typingObserver.observe(el);
        });

        // ============================================
        // SMOOTH REVEAL FOR HERO SECTION
        // ============================================
        const hero = document.querySelector('.hero');

        if (hero) {
            // Add fade-in class after short delay
            setTimeout(function() {
                hero.classList.add('fade-in');
            }, 100);
        }

        // ============================================
        // ANIMATE ON SCROLL DIRECTION
        // ============================================
        let lastScrollPosition = 0;

        window.addEventListener('scroll', function() {
            const currentScrollPosition = window.pageYOffset;

            if (currentScrollPosition > lastScrollPosition) {
                // Scrolling down
                document.body.classList.add('scroll-down');
                document.body.classList.remove('scroll-up');
            } else {
                // Scrolling up
                document.body.classList.add('scroll-up');
                document.body.classList.remove('scroll-down');
            }

            lastScrollPosition = currentScrollPosition;
        }, { passive: true });

        // ============================================
        // PERFORMANCE: REQUEST IDLE CALLBACK
        // ============================================
        if ('requestIdleCallback' in window) {
            requestIdleCallback(function() {
                // Preload critical images
                const criticalImages = document.querySelectorAll('[data-preload]');
                criticalImages.forEach(function(img) {
                    const tempImg = new Image();
                    tempImg.src = img.dataset.preload;
                });
            });
        }

        // ============================================
        // REDUCE MOTION PREFERENCE
        // ============================================
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        if (prefersReducedMotion) {
            // Disable animations for users who prefer reduced motion
            document.body.classList.add('reduce-motion');

            // Override animation classes
            const allAnimated = document.querySelectorAll('.fade-in-on-scroll, .slide-in-left, .slide-in-right');
            allAnimated.forEach(function(el) {
                el.style.animation = 'none';
                el.style.transition = 'none';
            });
        }

    });

})();
