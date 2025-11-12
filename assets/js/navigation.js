/**
 * Endpoint.US Navigation JavaScript
 * Handles mobile menu, dropdowns, and navigation interactions
 */

(function() {
    'use strict';

    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {

        // ============================================
        // MOBILE MENU TOGGLE
        // ============================================
        const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
        const mainNav = document.querySelector('.main-navigation');
        const hamburgerIcon = document.querySelector('.hamburger-icon');

        if (mobileMenuToggle && mainNav) {
            mobileMenuToggle.addEventListener('click', function() {
                const isExpanded = this.getAttribute('aria-expanded') === 'true';

                // Toggle aria-expanded
                this.setAttribute('aria-expanded', !isExpanded);

                // Toggle nav visibility
                mainNav.classList.toggle('active');

                // Animate hamburger icon
                hamburgerIcon.classList.toggle('active');

                // Prevent body scroll when menu is open
                if (!isExpanded) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            });
        }

        // ============================================
        // MOBILE DROPDOWN TOGGLES
        // ============================================
        const dropdownToggles = document.querySelectorAll('.has-dropdown > .nav-link');

        // Only add click handlers on mobile
        if (window.innerWidth < 768) {
            dropdownToggles.forEach(function(toggle) {
                toggle.addEventListener('click', function(e) {
                    e.preventDefault();
                    const parent = this.parentElement;
                    parent.classList.toggle('active');

                    // Close other open dropdowns
                    dropdownToggles.forEach(function(otherToggle) {
                        if (otherToggle !== toggle) {
                            otherToggle.parentElement.classList.remove('active');
                        }
                    });
                });
            });
        }

        // ============================================
        // CLOSE MENU ON OUTSIDE CLICK
        // ============================================
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.main-navigation') &&
                !e.target.closest('.mobile-menu-toggle') &&
                mainNav.classList.contains('active')) {
                mainNav.classList.remove('active');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });

        // ============================================
        // CLOSE MENU ON ESC KEY
        // ============================================
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && mainNav.classList.contains('active')) {
                mainNav.classList.remove('active');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
                mobileMenuToggle.focus();
                document.body.style.overflow = '';
            }
        });

        // ============================================
        // STICKY HEADER ON SCROLL
        // ============================================
        const siteHeader = document.querySelector('.site-header');
        let lastScrollTop = 0;
        let scrollTimeout;

        window.addEventListener('scroll', function() {
            clearTimeout(scrollTimeout);

            scrollTimeout = setTimeout(function() {
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

                // Add shadow when scrolled
                if (scrollTop > 50) {
                    siteHeader.classList.add('scrolled');
                } else {
                    siteHeader.classList.remove('scrolled');
                }

                lastScrollTop = scrollTop;
            }, 10);
        });

        // ============================================
        // SMOOTH SCROLL FOR ANCHOR LINKS
        // ============================================
        const anchorLinks = document.querySelectorAll('a[href^="#"]');

        anchorLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                const href = this.getAttribute('href');

                // Ignore empty anchors
                if (href === '#' || href === '#!') {
                    return;
                }

                const target = document.querySelector(href);

                if (target) {
                    e.preventDefault();

                    // Close mobile menu if open
                    if (mainNav.classList.contains('active')) {
                        mainNav.classList.remove('active');
                        mobileMenuToggle.setAttribute('aria-expanded', 'false');
                        document.body.style.overflow = '';
                    }

                    // Get header height for offset
                    const headerHeight = siteHeader.offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;

                    // Smooth scroll to target
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });

                    // Update focus for accessibility
                    target.setAttribute('tabindex', '-1');
                    target.focus();
                }
            });
        });

        // ============================================
        // HIGHLIGHT ACTIVE NAV LINK
        // ============================================
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-link');

        navLinks.forEach(function(link) {
            const linkPath = new URL(link.href).pathname;

            if (linkPath === currentPath ||
                (linkPath !== '/' && currentPath.startsWith(linkPath))) {
                link.classList.add('active');

                // If in dropdown, highlight parent too
                const parentDropdown = link.closest('.has-dropdown');
                if (parentDropdown) {
                    parentDropdown.querySelector('.nav-link').classList.add('active-parent');
                }
            }
        });

        // ============================================
        // KEYBOARD NAVIGATION FOR DROPDOWNS
        // ============================================
        const dropdownParents = document.querySelectorAll('.has-dropdown');

        dropdownParents.forEach(function(parent) {
            const parentLink = parent.querySelector(':scope > .nav-link');
            const dropdown = parent.querySelector('.mega-menu, .dropdown-menu');
            const dropdownLinks = dropdown ? dropdown.querySelectorAll('a') : [];

            // Open dropdown on Enter/Space
            parentLink.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    if (window.innerWidth >= 768) {
                        e.preventDefault();
                        parent.classList.toggle('keyboard-active');

                        if (parent.classList.contains('keyboard-active')) {
                            // Focus first link in dropdown
                            if (dropdownLinks[0]) {
                                dropdownLinks[0].focus();
                            }
                        }
                    }
                }
            });

            // Navigate through dropdown with arrow keys
            dropdownLinks.forEach(function(link, index) {
                link.addEventListener('keydown', function(e) {
                    if (e.key === 'ArrowDown') {
                        e.preventDefault();
                        const nextLink = dropdownLinks[index + 1];
                        if (nextLink) {
                            nextLink.focus();
                        }
                    } else if (e.key === 'ArrowUp') {
                        e.preventDefault();
                        if (index === 0) {
                            parentLink.focus();
                            parent.classList.remove('keyboard-active');
                        } else {
                            const prevLink = dropdownLinks[index - 1];
                            if (prevLink) {
                                prevLink.focus();
                            }
                        }
                    } else if (e.key === 'Escape') {
                        e.preventDefault();
                        parentLink.focus();
                        parent.classList.remove('keyboard-active');
                    }
                });
            });
        });

        // ============================================
        // HANDLE WINDOW RESIZE
        // ============================================
        let resizeTimeout;

        window.addEventListener('resize', function() {
            clearTimeout(resizeTimeout);

            resizeTimeout = setTimeout(function() {
                // Reset mobile menu on resize to desktop
                if (window.innerWidth >= 768) {
                    mainNav.classList.remove('active');
                    mobileMenuToggle.setAttribute('aria-expanded', 'false');
                    document.body.style.overflow = '';

                    // Remove mobile dropdown active classes
                    dropdownToggles.forEach(function(toggle) {
                        toggle.parentElement.classList.remove('active');
                    });
                }
            }, 250);
        });

        // ============================================
        // BREADCRUMB SCHEMA ENHANCEMENT
        // ============================================
        const breadcrumbItems = document.querySelectorAll('.breadcrumb li');

        breadcrumbItems.forEach(function(item, index) {
            const link = item.querySelector('a');

            if (link) {
                // Add schema attributes
                item.setAttribute('itemprop', 'itemListElement');
                item.setAttribute('itemscope', '');
                item.setAttribute('itemtype', 'https://schema.org/ListItem');

                link.setAttribute('itemprop', 'item');

                // Add position meta
                const position = document.createElement('meta');
                position.setAttribute('itemprop', 'position');
                position.setAttribute('content', (index + 1).toString());
                item.appendChild(position);

                // Add name span
                const nameSpan = document.createElement('span');
                nameSpan.setAttribute('itemprop', 'name');
                nameSpan.textContent = link.textContent;
                link.textContent = '';
                link.appendChild(nameSpan);
            }
        });

    });

})();
