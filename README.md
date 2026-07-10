# philips-Fitness

philips-Fitness is a Django full-stack website inspired by the Archipelago-Rugby team theme. It combines club-style branding, community content, and shop functionality into one responsive platform.

The project was built to satisfy the requirements of a full-stack milestone project. It includes user authentication, relational data handling, form validation, Stripe payment integration, and deployment-ready configuration.

## Table of Contents

- [Project Overview](#project-overview)
- [User Experience](#user-experience)
- [Design Goals](#design-goals)
- [Features](#features)
- [Database Design](#database-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Stripe Integration](#stripe-integration)
- [Credits](#credits)
- [References](#references)
- [Future Improvements](#future-improvements)

## Project Overview

The site was created to give the Archipelago-Rugby theme a practical and polished online home. Visitors can browse the site, read community updates, and view shop content, while registered users can access additional features.

The site structure reflects a real club environment, where content, membership, and products all live in one connected system.

## User Experience

The user experience is designed to be clean, direct, and easy to navigate. The layout supports both new visitors and returning users by keeping the main actions visible and the content easy to scan.

The design works across desktop and mobile screen sizes, with responsive cards, clear navigation, and simple content sections.

## Design Goals

The main design goal was to create a site that feels tied to a rugby club rather than a generic template. The visual style uses strong spacing, bold headings, and modern cards to give the site a more finished and branded feel.

The interface is intentionally simple so the content remains the focus.

## Features

- Responsive homepage with custom branding.
- Community post list page.
- Community post creation form.
- Shop page for products.
- User registration and login.
- Protected member features.
- Django admin management.
- Stripe payment support in test mode.
- Organised template structure.
- Custom CSS styling.

## Database Design

The project uses a relational database through Django models. The data structure is designed to support connected content such as users, profiles, posts, products, and purchases.

This allows the site to manage both public and restricted content in a structured way.

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- Django
- SQLite for local development
- PostgreSQL for deployment
- Stripe
- Git and GitHub

## Testing

Testing was carried out by checking:
- all main page links,
- form submission and validation,
- user login and sign-up behaviour,
- access to protected content,
- product and community page display,
- mobile responsiveness,
- styling consistency,
- Stripe checkout flow in test mode.

## Deployment

The project is prepared for deployment using Heroku. Sensitive values such as secret keys and Stripe keys should be stored as environment variables rather than committed to the repository.

Deployment includes:
- production settings,
- allowed hosts configuration,
- static file handling,
- database setup,
- and environment variable management.

## Stripe Integration

Stripe is used for test payment functionality. This gives the project a realistic e-commerce feature without using live payment details.

The payment flow is intended to let a user add items, proceed to checkout, and complete a test transaction successfully.

## Credits

- Django documentation
- Stripe documentation
- Any tutorials or code snippets used during development
- Any fonts, images, or icons used in the final project

## References


- images,
- fonts,
- tutorials,
- documentation,
- design inspiration.

## Future Improvements

- Add richer member-only functionality.
- Expand the shop with more products.
- Improve the profile system.
- Add more interactive community features.
- Refine the styling and animations further.
