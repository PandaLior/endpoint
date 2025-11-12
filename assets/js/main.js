/**
 * Endpoint.US Main JavaScript
 * General functionality and utilities
 */

(function() {
    'use strict';

    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {

        // ============================================
        // CONSOLE WELCOME MESSAGE
        // ============================================
        console.log('%cEndpoint.US', 'font-size: 24px; font-weight: bold; color: #4A90E2;');
        console.log('%cSecure Endpoint Security Services', 'font-size: 14px; color: #64748B;');

        // ============================================
        // EXTERNAL LINKS - OPEN IN NEW TAB
        // ============================================
        const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="endpoint.us.com"])');

        externalLinks.forEach(function(link) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');

            // Add visual indicator for external links
            if (!link.querySelector('.external-icon')) {
                const icon = document.createElement('span');
                icon.className = 'external-icon';
                icon.setAttribute('aria-label', '(opens in new tab)');
                icon.innerHTML = ' &#x2197;';
                link.appendChild(icon);
            }
        });

        // ============================================
        // COPY TO CLIPBOARD FUNCTIONALITY
        // ============================================
        const copyButtons = document.querySelectorAll('[data-copy]');

        copyButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const textToCopy = this.dataset.copy;

                navigator.clipboard.writeText(textToCopy).then(function() {
                    // Show success feedback
                    const originalText = button.textContent;
                    button.textContent = 'Copied!';
                    button.classList.add('success');

                    setTimeout(function() {
                        button.textContent = originalText;
                        button.classList.remove('success');
                    }, 2000);
                }).catch(function(err) {
                    console.error('Failed to copy:', err);
                });
            });
        });

        // ============================================
        // PRINT PAGE FUNCTIONALITY
        // ============================================
        const printButtons = document.querySelectorAll('[data-print]');

        printButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                window.print();
            });
        });

        // ============================================
        // MODAL FUNCTIONALITY
        // ============================================
        const modalTriggers = document.querySelectorAll('[data-modal]');
        const modals = document.querySelectorAll('.modal');
        const modalCloses = document.querySelectorAll('.modal-close');

        modalTriggers.forEach(function(trigger) {
            trigger.addEventListener('click', function(e) {
                e.preventDefault();
                const modalId = this.dataset.modal;
                const modal = document.getElementById(modalId);

                if (modal) {
                    modal.classList.add('active');
                    document.body.style.overflow = 'hidden';

                    // Focus first focusable element
                    const focusable = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
                    if (focusable[0]) {
                        focusable[0].focus();
                    }
                }
            });
        });

        modalCloses.forEach(function(closeBtn) {
            closeBtn.addEventListener('click', function() {
                const modal = this.closest('.modal');
                if (modal) {
                    modal.classList.remove('active');
                    document.body.style.overflow = '';
                }
            });
        });

        // Close modal on outside click
        modals.forEach(function(modal) {
            modal.addEventListener('click', function(e) {
                if (e.target === this) {
                    this.classList.remove('active');
                    document.body.style.overflow = '';
                }
            });
        });

        // Close modal on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const activeModal = document.querySelector('.modal.active');
                if (activeModal) {
                    activeModal.classList.remove('active');
                    document.body.style.overflow = '';
                }
            }
        });

        // ============================================
        // TABS FUNCTIONALITY
        // ============================================
        const tabButtons = document.querySelectorAll('[role="tab"]');
        const tabPanels = document.querySelectorAll('[role="tabpanel"]');

        tabButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const tabId = this.getAttribute('aria-controls');
                const tabGroup = this.closest('[role="tablist"]');

                // Update button states
                tabGroup.querySelectorAll('[role="tab"]').forEach(function(btn) {
                    btn.setAttribute('aria-selected', 'false');
                    btn.classList.remove('active');
                });

                this.setAttribute('aria-selected', 'true');
                this.classList.add('active');

                // Update panel visibility
                const container = this.closest('.tabs-container') || document;
                container.querySelectorAll('[role="tabpanel"]').forEach(function(panel) {
                    panel.hidden = true;
                    panel.classList.remove('active');
                });

                const targetPanel = document.getElementById(tabId);
                if (targetPanel) {
                    targetPanel.hidden = false;
                    targetPanel.classList.add('active');
                }
            });

            // Keyboard navigation for tabs
            button.addEventListener('keydown', function(e) {
                const tabGroup = this.closest('[role="tablist"]');
                const tabs = Array.from(tabGroup.querySelectorAll('[role="tab"]'));
                const currentIndex = tabs.indexOf(this);

                if (e.key === 'ArrowRight') {
                    e.preventDefault();
                    const nextTab = tabs[currentIndex + 1] || tabs[0];
                    nextTab.click();
                    nextTab.focus();
                } else if (e.key === 'ArrowLeft') {
                    e.preventDefault();
                    const prevTab = tabs[currentIndex - 1] || tabs[tabs.length - 1];
                    prevTab.click();
                    prevTab.focus();
                } else if (e.key === 'Home') {
                    e.preventDefault();
                    tabs[0].click();
                    tabs[0].focus();
                } else if (e.key === 'End') {
                    e.preventDefault();
                    tabs[tabs.length - 1].click();
                    tabs[tabs.length - 1].focus();
                }
            });
        });

        // ============================================
        // TOOLTIP FUNCTIONALITY
        // ============================================
        const tooltips = document.querySelectorAll('[data-tooltip]');

        tooltips.forEach(function(element) {
            const tooltipText = element.dataset.tooltip;
            const tooltip = document.createElement('span');
            tooltip.className = 'tooltip';
            tooltip.textContent = tooltipText;
            element.appendChild(tooltip);

            element.addEventListener('mouseenter', function() {
                tooltip.classList.add('visible');
            });

            element.addEventListener('mouseleave', function() {
                tooltip.classList.remove('visible');
            });

            // Keyboard support
            element.addEventListener('focus', function() {
                tooltip.classList.add('visible');
            });

            element.addEventListener('blur', function() {
                tooltip.classList.remove('visible');
            });
        });

        // ============================================
        // FORM VALIDATION HELPERS
        // ============================================
        const forms = document.querySelectorAll('form[data-validate]');

        forms.forEach(function(form) {
            form.addEventListener('submit', function(e) {
                let isValid = true;

                // Email validation
                const emailFields = form.querySelectorAll('input[type="email"]');
                emailFields.forEach(function(field) {
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailRegex.test(field.value)) {
                        isValid = false;
                        showFieldError(field, 'Please enter a valid email address');
                    } else {
                        clearFieldError(field);
                    }
                });

                // Phone validation
                const phoneFields = form.querySelectorAll('input[type="tel"]');
                phoneFields.forEach(function(field) {
                    const phoneRegex = /^[\d\s\-\(\)]+$/;
                    if (field.value && !phoneRegex.test(field.value)) {
                        isValid = false;
                        showFieldError(field, 'Please enter a valid phone number');
                    } else {
                        clearFieldError(field);
                    }
                });

                // Required fields
                const requiredFields = form.querySelectorAll('[required]');
                requiredFields.forEach(function(field) {
                    if (!field.value.trim()) {
                        isValid = false;
                        showFieldError(field, 'This field is required');
                    } else {
                        clearFieldError(field);
                    }
                });

                if (!isValid) {
                    e.preventDefault();

                    // Focus first invalid field
                    const firstError = form.querySelector('.field-error');
                    if (firstError) {
                        const field = firstError.previousElementSibling;
                        if (field) {
                            field.focus();
                        }
                    }
                }
            });

            // Real-time validation
            const fields = form.querySelectorAll('input, textarea, select');
            fields.forEach(function(field) {
                field.addEventListener('blur', function() {
                    if (this.hasAttribute('required') && !this.value.trim()) {
                        showFieldError(this, 'This field is required');
                    } else {
                        clearFieldError(this);
                    }
                });
            });
        });

        function showFieldError(field, message) {
            clearFieldError(field);

            field.classList.add('error');
            field.setAttribute('aria-invalid', 'true');

            const errorDiv = document.createElement('div');
            errorDiv.className = 'field-error';
            errorDiv.textContent = message;
            errorDiv.setAttribute('role', 'alert');

            field.parentNode.insertBefore(errorDiv, field.nextSibling);
        }

        function clearFieldError(field) {
            field.classList.remove('error');
            field.removeAttribute('aria-invalid');

            const existingError = field.parentNode.querySelector('.field-error');
            if (existingError) {
                existingError.remove();
            }
        }

        // ============================================
        // CURRENT YEAR IN FOOTER
        // ============================================
        const yearElements = document.querySelectorAll('[data-year]');
        const currentYear = new Date().getFullYear();

        yearElements.forEach(function(el) {
            el.textContent = currentYear;
        });

        // ============================================
        // DETECT BROWSER FOR DEBUGGING
        // ============================================
        const userAgent = navigator.userAgent;
        let browserClass = '';

        if (userAgent.indexOf('Chrome') > -1) {
            browserClass = 'browser-chrome';
        } else if (userAgent.indexOf('Safari') > -1) {
            browserClass = 'browser-safari';
        } else if (userAgent.indexOf('Firefox') > -1) {
            browserClass = 'browser-firefox';
        } else if (userAgent.indexOf('MSIE') > -1 || userAgent.indexOf('Trident') > -1) {
            browserClass = 'browser-ie';
        } else if (userAgent.indexOf('Edge') > -1) {
            browserClass = 'browser-edge';
        }

        if (browserClass) {
            document.documentElement.classList.add(browserClass);
        }

        // ============================================
        // PERFORMANCE MONITORING
        // ============================================
        if ('performance' in window && 'PerformanceObserver' in window) {
            // Log Core Web Vitals to console in development
            const observer = new PerformanceObserver(function(list) {
                for (const entry of list.getEntries()) {
                    if (entry.entryType === 'paint') {
                        console.log(entry.name + ':', entry.startTime + 'ms');
                    }
                }
            });

            observer.observe({ entryTypes: ['paint', 'navigation'] });

            // Report when page is fully loaded
            window.addEventListener('load', function() {
                const perfData = performance.timing;
                const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
                console.log('Page load time:', pageLoadTime + 'ms');
            });
        }

        // ============================================
        // ACCESSIBILITY: SKIP LINKS
        // ============================================
        const skipLinks = document.querySelectorAll('.skip-to-content');

        skipLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                const target = document.querySelector(this.getAttribute('href'));

                if (target) {
                    e.preventDefault();
                    target.setAttribute('tabindex', '-1');
                    target.focus();

                    // Smooth scroll to target
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // ============================================
        // INITIALIZE THIRD-PARTY SCRIPTS
        // ============================================
        // Elfsight forms are already loaded via async script tag

        // ============================================
        // SERVICE WORKER REGISTRATION (if applicable)
        // ============================================
        if ('serviceWorker' in navigator && window.location.protocol === 'https:') {
            // Uncomment to enable service worker
            /*
            navigator.serviceWorker.register('/sw.js').then(function(registration) {
                console.log('Service Worker registered:', registration);
            }).catch(function(error) {
                console.log('Service Worker registration failed:', error);
            });
            */
        }

    });

    // ============================================
    // PAGE VISIBILITY API
    // ============================================
    document.addEventListener('visibilitychange', function() {
        if (document.hidden) {
            // Page is hidden
            console.log('Page hidden');
        } else {
            // Page is visible
            console.log('Page visible');
        }
    });

})();
