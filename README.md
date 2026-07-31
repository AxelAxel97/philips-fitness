# Archipelago Rugby

Archipelago Rugby is a Django full-stack web application built around a modern rugby club theme. The project combines club branding, community interaction, shop content, user authentication, and subscription functionality into one responsive platform.

The site was developed as a milestone full-stack project and includes key features expected in a database-driven web application, including relational models, user accounts, protected content, form handling, admin management, and Stripe subscription payments in test mode.

---

## Table of Contents

- [Project Overview](#project-overview)
- [User Experience](#user-experience)
- [Design Goals](#design-goals)
- [Site Goals](#site-goals)
- [Target Audience](#target-audience)
- [Features](#features)
- [Database Design](#database-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Stripe Integration](#stripe-integration)
- [Deployment](#deployment)
- [Credits](#credits)
- [References](#references)
- [Future Improvements](#future-improvements)

---

## Project Overview

The project was created to give the Archipelago Rugby concept a practical and visually branded online home. The aim was to build a site that feels like a real rugby club platform rather than a generic starter template.

Visitors can explore the site, browse community and shop content, and view the sponsor area. Registered users can log in, interact with protected areas of the site, and complete a Stripe subscription flow in sandbox mode.

The overall site structure reflects a club environment where public content, member features, supporter subscriptions, and admin control all exist within one connected Django application.

---

## User Experience

The user experience was designed to be clear, direct, and easy to navigate. The main navigation remains visible across the site so users can move quickly between the home page, community area, shop, sponsor page, and admin tools.

The layout uses bold headings, spacious cards, and a clear visual hierarchy so that important actions are easy to spot. The interface avoids unnecessary complexity and keeps the focus on the core content and site purpose.

The design also supports responsive behaviour across different screen sizes, helping the project feel more polished and usable on both desktop and mobile devices.

---

## Design Goals

The main design goal was to create a sports-themed platform with stronger club identity than a default Django project. The site styling was shaped around a rugby club atmosphere with clear branding, bold typography, and a more premium-looking layout.

A second design goal was consistency. Shared layout elements such as the header, navigation, message alerts, and footer were reused across pages so the site feels like one connected experience.

A third goal was practicality. The project needed to satisfy full-stack coursework requirements while still looking like a believable real-world platform.

---

## Site Goals

The main site goals were:

- To create a branded full-stack Django website with multiple connected apps.
- To provide public-facing content alongside protected user functionality.
- To demonstrate relational database use through connected Django models.
- To implement a working authentication system.
- To include Stripe payment functionality in test mode.
- To produce a project that could be documented, tested, and prepared for deployment.

---

## Target Audience

The target audience for the site includes:

- Visitors interested in a rugby club or sports community.
- Users who want to browse updates and club-related content.
- Supporters who may want to subscribe as sponsors.
- Administrators who need to manage content, users, and data through Django admin.

The platform is designed to feel approachable for casual visitors while still supporting logged-in and subscriber-based behaviour behind the scenes.

---

## Features

### Global Features

- Shared base template with site-wide navigation and footer.
- Responsive structure across major pages.
- Styled success, warning, and error messages using Django messages.
- Archipelago Rugby branding across templates and content sections.

### Home Page

- Branded landing page introducing the club theme.
- Strong hero section and supporting content.
- Clear top-level navigation to the rest of the site.

### Community App

- Community post list page.
- Community post creation functionality.
- Protected user access for subscriber/member-related behaviour.
- Structured content flow for club-style updates.

### Shop App

- Product-focused page for club merchandise or related content.
- Integrated into the wider site structure through shared templates.
- Supports the e-commerce direction of the project.

### Accounts App

- User sign-up and login functionality.
- Profile model connected to Django users.
- Subscriber flag stored on the user profile.

### Subscription App

- Sponsor/subscription page with a clear call-to-action.
- Stripe Checkout session creation through Django.
- Redirect to Stripe-hosted checkout page in sandbox mode.
- Success and cancellation pages for the subscription flow.
- Subscription activation logic after successful checkout.

### Admin Features

- Django admin access for data management.
- Ability to manage users, profiles, subscriptions, and other site content through the admin interface.

---

## Database Design

The project uses Django’s ORM with a relational database structure. The data model is designed to support connected content and user-based functionality across the site.

Core relationships include:

- A `User` model connected to a `Profile`.
- A `Profile` model storing subscriber-related information.
- A `Subscription` model connected to the logged-in user.
- Community-related models for post content.
- Shop-related models for products and related content.

This relational structure allows the application to manage both public and protected content in an organised way. It also supports the project requirement for relational data handling in a full-stack application.

---

## Technologies Used

### Languages

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks and Libraries

- Django
- Stripe Python library

### Database

- SQLite for local development
- PostgreSQL intended for deployment

### Tools and Platforms

- Git
- GitHub
- VS Code
- Stripe
- Django admin

---

## Testing

Testing was carried out throughout development to confirm that the main site features, page navigation, user authentication, and Stripe subscription flow worked as expected.

### Manual Testing

#### Navigation and page rendering

| Feature | Action | Expected Result | Outcome |
|---|---|---|---|
| Home page | Open the site homepage | Homepage loads correctly with navigation, hero content, and branding | Pass |
| Community page | Click the Community link in the navbar | Community page opens correctly | Pass |
| Shop page | Click the Shop link in the navbar | Shop page opens correctly | Pass |
| Sponsor page | Click the Become a Sponsor link in the navbar | Sponsor page opens with sponsor information and checkout button | Pass |

#### Authentication and user access

| Feature | Action | Expected Result | Outcome |
|---|---|---|---|
| Login protection | Attempt protected sponsor checkout behaviour as a logged-out user | User cannot complete the protected action without authentication | Pass |
| Logged-in checkout access | Log in and click the sponsor checkout button | Logged-in user can begin the Stripe checkout process | Pass |
| Profile subscriber update | Complete the Stripe subscription flow in sandbox mode | User profile is updated to subscriber status in the success flow | Pass |

#### Stripe subscription testing

| Feature | Action | Expected Result | Outcome |
|---|---|---|---|
| Stripe configuration check | Click the sponsor button before Stripe values were configured | A Stripe configuration error is displayed | Pass |
| Checkout session creation | Add Stripe test keys and price ID, then click sponsor button | Stripe Checkout session is created and user is redirected to checkout | Pass |
| Stripe checkout page | Open checkout in sandbox mode | Stripe-hosted payment form loads correctly | Pass |
| Test payment | Use Stripe test card `4242 4242 4242 4242`, future expiry date, any CVC | Test payment is accepted in sandbox mode | Pass |
| Success redirect | Complete the payment flow | User is redirected back to the local success page | Pass |
| Success message | View the returned success page | Confirmation message is displayed to the user | Pass |

### Bugs Found and Fixed

#### Sponsor button appeared inactive
At one stage, the sponsor button appeared to do nothing when clicked. This turned out not to be a button issue, but a lack of visible Django messages in the shared template. After adding a Django messages block to the base template, Stripe errors became visible and debugging became much easier.

#### Missing Stripe keys
Once error messages were visible, Stripe returned an authentication error stating that no API key had been provided. This was caused by empty Stripe environment variables in the `.env` file. The issue was resolved by creating a Stripe sandbox account and adding the required keys.

#### Product ID versus Price ID confusion
During Stripe setup, the recurring sponsor product was created successfully, but the product identifier shown first was the Product ID rather than the Price ID needed by the Django checkout view. After locating the correct recurring `price_...` value and adding it to the `.env` file, the checkout flow worked correctly.

### Stripe Test Evidence

The Stripe subscription flow was successfully tested in sandbox mode. Testing confirmed that the sponsor button created a Stripe Checkout session, redirected to Stripe Checkout, accepted a sandbox payment, returned to the success page, and displayed a successful activation message.

### Remaining Limitation

The current success flow updates the subscription when the success URL is reached. In a more production-ready implementation, Stripe webhooks would normally be used to verify payment more securely. For the purposes of this project, the sandbox checkout flow still demonstrates working Stripe subscription integration.

---

## Stripe Integration

Stripe is used to provide subscription functionality in test mode. The project includes a sponsor page which posts to a Django view that creates a Stripe Checkout session for a recurring subscription product.

The integration currently includes:

- Stripe public and secret key configuration through environment variables.
- A recurring subscription product created in Stripe sandbox mode.
- A Stripe Checkout redirect flow.
- A local success page after payment.
- Subscription and profile updates in the Django success view.

This gives the project a realistic example of payment platform integration without using live customer payments.

---

## Deployment

The project is structured so it can be deployed with environment-based configuration. Sensitive values such as Django secret keys and Stripe credentials are intended to be stored in environment variables rather than committed to the repository.

Deployment preparation includes:

- environment variable usage,
- deployment-ready configuration structure,
- allowed hosts configuration,
- static file handling,
- database configuration,
- and separation of secret values from source code.

For a full deployment, the following areas would need to be confirmed and finalised:

- production database configuration,
- deployment platform settings,
- static and media file handling,
- debug turned off in production,
- and all required environment variables added to the host platform.

---

## Credits

- Django documentation
- Stripe documentation
- Code Institute learning material if applicable
- Any tutorials referenced during development
- Any external assets used in the final design, including images, icons, and fonts

---

## References

The following source types informed the project:

- Django documentation
- Stripe documentation
- Design inspiration references
- Tutorials consulted during development
- Image sources used in the visual design
- Font or icon providers used in the interface

---

## Future Improvements

- Add webhook verification for stronger production-grade Stripe handling.
- Expand the shop with richer product data and images.
- Improve profile customisation and account management.
- Add more advanced member-only and subscriber-only features.
- Improve the community area with richer posting options.
- Strengthen visual polish and page-by-page refinement.
- Complete and document full deployment workflow.
