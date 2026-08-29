# Archipelago Rugby

Archipelago Rugby is a Django full-stack web application built around a modern rugby club theme. The project combines club branding, community interaction, shop content, user authentication, and sponsor subscription functionality into one responsive platform.

The site was developed as a milestone full-stack project and includes key database-driven features such as relational models, form handling, protected content, user accounts, admin management, and Stripe subscription payments in test mode. The aim was to build a platform that feels like a believable rugby club website rather than a generic starter project.

[Live Project](ADD_LIVE_LINK_HERE)  
[Repository](ADD_GITHUB_REPO_LINK_HERE)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Planning](#project-planning)
- [Strategy Plane](#strategy-plane)
- [Scope Plane](#scope-plane)
- [Structure Plane](#structure-plane)
- [Skeleton Plane](#skeleton-plane)
- [Surface Plane](#surface-plane)
- [User Stories](#user-stories)
- [Features](#features)
- [Database Design](#database-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Stripe Integration](#stripe-integration)
- [Credits](#credits)
- [References](#references)
- [Future Improvements](#future-improvements)

---

## Project Overview

The project was created to give the Archipelago Rugby concept a practical and visually branded online home. The aim was to build a site that feels like a real rugby club platform rather than a generic starter template.

Visitors can explore the site, browse community and shop content, and view the sponsor area. Registered users can log in, interact with protected areas of the site, and complete a Stripe subscription flow in sandbox mode.

The overall site structure reflects a club environment where public content, member features, supporter subscriptions, and admin control all exist within one connected Django application.

---

## Project Planning

Planning for this project was guided by the goal of creating a full-stack site that was both technically valid and visually believable. Rather than producing a simple collection of pages, the intention was to build a project with a clear identity, a practical user flow, and enough back-end logic to demonstrate meaningful full-stack development.

The planning process was shaped around the five planes model of user experience design. This made it easier to think about the site not only as code and features, but also as a structured user-facing product with goals, layout, logic, and presentation.

This also helped keep the project focused, especially because the scope needed to remain realistic for a milestone submission while still showing enough depth to satisfy the assessment requirements.

---

## Strategy Plane

### The Big Picture

The first stage of planning was to define what kind of site Archipelago Rugby should be. The project needed to feel more distinctive than a default sports template, while still supporting the technical requirements of a full-stack web application.

The concept developed into a rugby-club themed platform that could combine:

- public-facing content,
- community interaction,
- a shop section,
- user accounts,
- and a sponsor subscription flow.

### User Goals

The target user should be able to:

- understand what the site represents as soon as they arrive,
- move between the key areas of the site easily,
- browse club updates and merchandise,
- create an account and log in securely,
- and complete the sponsor subscription process without confusion.

### Site Owner Goals

From the site owner perspective, the project should:

- present a stronger club identity than a generic course project,
- allow content and users to be managed through Django admin,
- demonstrate relational database design,
- and include a realistic commercial or revenue-related feature through Stripe.

### Why this project idea worked well

A rugby-club site works well as a full-stack milestone because it naturally supports multiple apps and content types. It gives strong justification for having public content, member-only behaviour, products, profiles, and subscriptions all within the same connected project.

---

## Scope Plane

To manage scope effectively, the project was built around a practical MVP first. The aim was to create a polished and functional version of the core idea before considering richer extra features.

### MVP priorities

The minimum viable product focused on:

- a branded Django site structure,
- multiple connected apps,
- user sign-up and login,
- community content,
- shop content,
- a sponsor page,
- a Stripe-powered subscription flow in test mode,
- and admin management through Django admin.

### Features that were important but secondary

These included:

- more advanced profile tools,
- deeper member-only functionality,
- more polished animations,
- broader product content,
- and more interactive community features.

### Scope control

This project could easily have expanded too far if every possible sports-club feature had been included. Keeping the focus on authentication, relational models, sponsor subscriptions, community content, and shop presentation helped maintain a balance between ambition and completion.

---

## Structure Plane

The structure of the site was designed so that the user journey feels simple and easy to follow. The user should be able to understand the site’s purpose quickly and move from discovery to account access or sponsorship with very little friction.

The overall information architecture can be understood through four main areas:

1. **Landing and branding**  
   The homepage establishes the rugby-club identity and introduces the tone of the platform.

2. **Content and community**  
   The community area supports the club atmosphere and gives the site more life than a static brochure.

3. **Shop and sponsor flow**  
   The shop gives the project an e-commerce direction, while the sponsor page acts as the main subscription/payment journey.

4. **Accounts and admin**  
   User accounts support protected features, and Django admin supports practical data management.

This approach made the site easier to explain, easier to test, and easier to expand later.

---

## Skeleton Plane

### Wireframes and layout planning

Wireframes were used as planning tools to decide page structure, visual hierarchy, and layout consistency before refining the final design. The aim was not to create pixel-perfect design documents, but to map the key areas of each page clearly enough to support the build.

The wireframes focused on:

- shared navigation,
- strong hero/header areas,
- card-based content sections,
- sponsor call-to-action placement,
- and keeping layouts readable across screen sizes.

### Detailed wireframe coverage

The following page wireframes were planned across **desktop, tablet, and mobile** views:

- Home page
- Community page
- Shop page
- Sponsor / subscription page
- Sign-up page
- Sign-in page
- Sign-out page
- Success page
- Error / empty-state views where relevant

### Home page wireframe

The home page wireframe was designed around a strong top section that introduces the site immediately. The page then moves into supporting branded sections that guide the user toward the rest of the platform.

The wireframe included:

- top navigation,
- hero section,
- supporting club identity content,
- quick access to community / shop / sponsor areas,
- and footer navigation.

### Community page wireframe

The community page wireframe was designed to feel structured and readable rather than cluttered. The aim was to create a clear area for post content and post creation without confusing first-time users.

The wireframe included:

- page heading,
- post list area,
- create-post access or form area,
- and shared navigation around it.

### Shop page wireframe

The shop page wireframe focused on product visibility and card consistency. Product tiles needed enough space for titles, imagery, and supporting details while still remaining responsive.

The wireframe included:

- page heading,
- product card grid,
- clear spacing between product blocks,
- and shared header/footer structure.

### Sponsor page wireframe

The sponsor page wireframe was particularly important because it supports the Stripe flow. This page needed to present sponsor information clearly while also keeping the call-to-action prominent.

The wireframe included:

- sponsor heading and explanatory text,
- a clear sponsor or subscribe button,
- reassurance or supporting copy,
- and space for success/error messages where relevant.

### Authentication page wireframes

The sign-up, sign-in, and sign-out wireframes were designed to be simple and familiar. These pages did not need heavy decoration; instead, they needed clarity, accessibility, and consistency with the rest of the project styling.

The authentication wireframes included:

- page title,
- form block,
- helper text,
- navigation back into the main site,
- and a clean single-column structure on mobile.

### Responsive considerations

The wireframes were adapted for desktop, tablet, and mobile layouts. The main differences across device sizes were:

- stacked sections on smaller screens,
- narrower card and form widths,
- preserved spacing and readability,
- and simplified visual flow where multiple columns would have become cramped.

### Wireframe images

Add your actual wireframe screenshots here, for example:

- `Home page – desktop, tablet, mobile`
- `Community page – desktop, tablet, mobile`
- `Shop page – desktop, tablet, mobile`
- `Sponsor page – desktop, tablet, mobile`
- `Authentication pages – desktop, tablet, mobile`

**Add wireframe screenshots below this section before submission.**

---

## Surface Plane

### Final look and feel

The final visual style was built around the idea that Archipelago Rugby should feel like a club with a recognisable presence, not just a coursework submission. The design uses stronger headings, structured spacing, and a cleaner card-based layout to create a more polished look.

### Colour and branding direction

The project aimed for a sports-club visual identity that felt bold and grounded. The design direction focused on brand consistency across templates rather than overly decorative styling.

### Typography and layout

Typography was used to support hierarchy and readability, especially across responsive layouts. The visual approach prioritised:

- clear headings,
- easy-to-scan sections,
- spacious layout blocks,
- and reusable design patterns across pages.

### Design intention

The interface was intentionally kept relatively simple so that the content remained the focus. The goal was not to overload the site with visual effects, but to make it feel more refined and more complete than a default Django project.

---

## User Stories

### First-Time Visitor

As a first-time visitor, I want to:

- understand what the site is about immediately,
- navigate clearly between pages,
- explore the club and community content,
- and find the main calls to action quickly.

### Returning Visitor

As a returning visitor, I want to:

- move around the site easily,
- recognise the key sections quickly,
- and access my account or sponsor options without confusion.

### Registered User

As a registered user, I want to:

- create an account and log in securely,
- access protected features,
- complete the sponsor subscription flow,
- and receive clear feedback when actions succeed or fail.

### Site Admin

As a site admin, I want to:

- manage models through Django admin,
- keep site content and users organised,
- and support the smooth running of the platform without editing code directly.

---

## Features

### Global Features

- Shared base template with site-wide navigation and footer.
- Responsive structure across major pages.
- Styled success, warning, and error messages using Django messages.
- Archipelago Rugby branding across templates and content sections.

### Home Page

The home page acts as the landing page for the entire project. It introduces the club branding, sets the tone for the site, and directs the user toward the main content areas.

Key features include:

- branded hero section,
- supporting introductory content,
- and clear navigation to the rest of the platform.

### Community App

The community section helps the site feel more like a real club space rather than a static brochure website. It introduces content that can feel club-led or user-led depending on how the project evolves.

Key features include:

- community post list page,
- community post creation functionality,
- protected user access where relevant,
- and structured content flow for club-style updates.

### Shop App

The shop section supports the e-commerce direction of the project and makes the site feel more complete. Product imagery and card layouts help strengthen this section visually.

Key features include:

- product-focused page for club merchandise or related items,
- integration with the wider site layout,
- and a stronger branded presentation through product images and content.

### Accounts App

The accounts system supports the distinction between public and authenticated users.

Key features include:

- user sign-up and login,
- profile model linked to Django users,
- and subscriber status stored on the user profile.

### Subscription App

The subscription system is one of the strongest full-stack features in the project because it combines templates, views, configuration, and third-party integration.

Key features include:

- sponsor page with a clear call-to-action,
- Stripe Checkout session creation through Django,
- redirect to Stripe-hosted checkout in sandbox mode,
- success and cancellation handling,
- and subscription activation logic after a successful checkout.

### Admin Features

Django admin supports the practical management side of the platform.

Admin features include:

- user management,
- profile management,
- subscription visibility,
- and access to the project’s core site models.

---

## Database Design

The project uses Django’s ORM with a relational database structure. The data model supports connected content and user-based functionality across the site.

Core relationships include:

- a `User` model connected to a `Profile`,
- a `Profile` model storing subscriber-related information,
- a `Subscription` model connected to the logged-in user,
- community-related models for post content,
- and shop-related models for products and related records.

This relational structure allows the application to manage both public and protected content in an organised way. It also supports the project requirement for meaningful relational data handling within a full-stack web application.

If you created an ERD, insert it here.

**Add ERD image here before submission.**

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

### Additional Tools

Add any you actually used, such as:

- Figma for wireframes,
- image generation tools,
- icon libraries,
- validation tools,
- or design references.

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

## Deployment

The project is structured so it can be deployed with environment-based configuration. Sensitive values such as Django secret keys and Stripe credentials are intended to be stored in environment variables rather than committed to the repository.

### Deployment Preparation

Deployment preparation includes:

- environment variable usage,
- deployment-ready configuration structure,
- allowed hosts configuration,
- static file handling,
- database configuration,
- and separation of secret values from source code.

### Typical deployment checklist

For a full deployment, the following areas would need to be confirmed and finalised:

- production database configuration,
- deployment platform settings,
- static and media file handling,
- debug turned off in production,
- and all required environment variables added to the host platform.

### Cloning the project

```bash
git clone ADD_REPO_URL_HERE
cd Archipelago-Rugby
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
