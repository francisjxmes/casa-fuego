# **Casa Fuego - Restauartant Booking System**

A full-stack Django web application that allows customers to browse the restaurant menu, create an account, and make online table bookings. Users can view, edit, and cancel their bookings through a secure account dashboard. The site owner can accept online reservations while preventing double-bookings and maintaining reliable reservation data.

---

## Live Site

The project is deployed on Render and can be accessed here:
[Casa Fuego Live Website](https://casa-fuego-1.onrender.com/)

## **1. Project Goals**

### **User Goals**
- Book a table online quickly and easily  
- See available times without errors or double-bookings  
- Manage, edit, and cancel their bookings  
- View the restaurant menu  
- Access all features from mobile and desktop

### **Site Owner Goals**
- Provide a modern online booking system  
- Avoid double reservations  
- Allow users to register and log in securely  
- Allow customers to manage their own bookings  
- Ensure bookings are stored safely in the database 

--- 

# **2. UX (User Experience)**  
Following the UXD principles and the Five Planes model.

## **2.1 Strategy Plane**

### **Target Users**
- Restaurant customers  
- People booking meals with friends/family  
- Mobile-first users  
- Customers who prefer quick, online booking over calling  

### **User Needs**
- Straightforward booking system  
- Ability to amend bookings  
- Clear feedback when a booking is confirmed or rejected  
- Easy-to-read menu  

### **Business Needs**
- Reduce staff time spent handling reservations  
- Prevent scheduling conflicts  
- Increase customer engagement  
- Provide a professional online presence

---

## **2.2 Scope Plane**

### **Core Features**
- User authentication (login, signup, logout)  
- Booking form with validation  
- Booking conflict detection  
- Edit booking  
- Delete booking  
- View past and future bookings  
- Responsive navigation & mobile menu  
- Menu page  
- Success confirmation page  

### **Future Features (Nice to Have)**
- Email confirmation notifications  
- Staff admin panel for managing bookings  
- Payment integration  
- Table selection  
- Booking calendar UI

---

## **2.3 Structure Plane**

### **User Flow**
1. User lands on homepage  
2. Navigates to menu or booking page  
3. If not logged in → prompted to sign in/sign up  
4. Creates booking → booking validated → success page  
5. User can view/edit/cancel from “My Bookings”  

### **Information Architecture**
- Home  
- Menu  
- Booking Form  
- Login / Signup  
- My Bookings (CRUD interface)  

---

## **2.4 Skeleton Plane**

### **Wireframes**  
- **Homepage Wireframe:**  
![Homepage Wireframe Screenshot](/casa_fuego/bookings/static/images/home-wf.png)

- **Menu Page Wireframe:**  
![Menu Wirefram Screenshot](/casa_fuego/bookings/static/images/menu-wf.png)

- **Booking Form Wireframe:**  
![Booking Forrm Wireframe Screenshot](/casa_fuego/bookings/static/images/booking-wf.png)    

- **Login / Signup Wireframe:**  
![Login Wireframe Screenshot](/casa_fuego/bookings/static/images/login-wf.png)   

- **My Bookings (CRUD) Wireframe:**  
![Signup Wireframe Screenshot](/casa_fuego/bookings/static/images/signup-wf.png)   

---

## **2.5 Surface Plane**

- Dark, modern theme with warm tones  
- Decorative stylised logo  
- High contrast text for readability  
- Clean input fields & clear CTAs  
- Fully responsive layout  
- Mobile hamburger menu with slide-out panel  

---

 **3. User Stories**

### **Epic: Booking Management**
- As a user, I want to make a booking online so I don’t need to call.  
- As a user, I want to prevent double-bookings so I know my reservation is confirmed.  
- As a user, I want to edit a booking so I can change my plans.  
- As a user, I want to cancel a booking if I can no longer attend.  

### **Epic: User Authentication**
- As a user, I want to sign up securely so my data is protected.  
- As a user, I want to log in/out easily so I can manage my bookings.  
- As a user, I want feedback if my login fails.  

### **Epic: Navigation & Access**
- As a user, I want a mobile menu so I can navigate on my phone.  
- As a user, I want the menu page easily accessible so I can view food options.  

### **Site Owner**
- As the site owner, I want all bookings stored in a database so I can manage capacity.  

---

### **Booking Model**

The project uses a single main model, Booking, which stores all customer reservation details.
Each booking includes the customer’s name, party size, date, and time.
If a user is logged in, the booking is linked to their account so they can view, edit, or cancel their reservations.

This model is lightweight, easy to manage, and suitable for the scale of a small restaurant booking system.

### **ERD**

The data structure in this project is intentionally simple.
There is only one core model, Booking, and it has an optional relationship to Django’s built-in User model.

This means:

- A User can have many Bookings

- A Booking can belong to one User (or none if the customer booked without logging in)

# **5. Features**

### **Implemented Features**
- Responsive navbar & mobile side panel  
- Menu page  
- Booking form  
- Input validation  
- Conflict prevention (date + time)  
- Booking success page  
- CRUD: Create, Read, Update, Delete bookings  
- Authentication (login/signup/logout)  
- Custom styled login/signup pages  
- Whitenoise static files on Render  
- Protected routes using @login_required  

### **Future Features**
- Email reminders  
- Table selection  
- Admin management panel  
- Booking calendar UI  

---

## **Manual Testing**

### **Navigation & Responsiveness**
- Each navigation link was clicked individually (Home, Menu, Book, My Bookings, Login, Logout) to confirm they all loaded the correct pages.

- The Casa Fuego logo was clicked to ensure it redirected back to the homepage.

- On mobile screen sizes, the hamburger icon was tested:

    - When tapped, the side-panel opens as expected.

    - The close button correctly closes the panel.

    - Tapping outside the panel also closes it.

- All navigation elements were tested for responsiveness on multiple screen sizes.

All navigation and responsive elements worked as expected.

---

### **Booking Form**

- The booking form loads correctly with all fields visible (name, party size, date, time).

- Attempting to select a date in the past correctly triggers the validation error: “You cannot book a date in the past.”

- Attempting to book a date and time that already exists triggers the correct error message: “Sorry, that time is already booked!”

- Submitting a fully valid booking redirects the user to the Booking Success page.

- The booking success page displays the correct confirmation message and return button.

---

### **My Bookings Page**

- Only bookings belonging to the authenticated user are displayed.

- Each booking entry shows the correct details (name, party size, date, time).

- The Edit button correctly loads the edit form with pre-populated booking data.

- Saving changes successfully updates the booking and returns to the bookings list.

- The Cancel button opens the delete confirmation page.

- Confirming the delete action removes the booking and updates the list.

All CRUD operations for bookings worked successfully.

---

### **Authentication (django-allauth)**

- A new account was successfully created via the signup page.

- Logging in with valid credentials works and redirects properly.

- Logging out returns the user to the site in a logged-out state.

- Attempting to access a protected page (such as /booking/ or /bookings/) while logged out correctly redirects to the login page.

- Entering incorrect login details displays the expected error message.

Authentication behaves correctly in all scenarios.

---

### **Frontend Validation**

- All pages were checked through the W3C HTML Validator. No major errors were present.

- The W3C CSS Validator was used, and after minor correction, the stylesheet passed with no errors.

- The browser console was checked for warnings or blocking errors. No critical issues were found.

---

### **Lighthouse Audits**

- Lighthouse tests were run on the main pages.

- Accessibility scored well, with labelled form fields and adequate contrast.

- SEO checks passed with good structure and metadata.

- Best Practices scored highly, with no security warnings.

- Performance was lower due to image sizes and natural Django load time, but still within acceptable limits for project requirements.

---

### **Deployment Verification (Render)**

- The site successfully deployed on Render with no build errors.

- Static files were correctly collected and served via WhiteNoise.

- PostgreSQL connection was tested by creating, editing, and deleting bookings directly on the live site.

- All environment variables were confirmed working (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL).

- The website was tested live on both desktop and mobile devices.

- Deployment was successful and fully functional.

## **Validator Testing**

- **HTML:** Passed  
- **CSS:** Passed after fixing minor issues  
- **Python PEP8:** No major issues  
- **Lighthouse:**  
  - Accessibility: 85  
  - SEO: 90  
  - Best Practices: 100  
  - Performance: 59  

---

# **8. Deployment (Render)**

### **Steps Taken**

1. Created GitHub repo  
2. Connected repo to Render  
3. Added environment variables:  
   ```
   PYTHON_VERSION = 3.12.1
   DEBUG = False
   ```
4. Build Command:
   ```
   pip3 install -r requirements.txt && python manage.py collectstatic --noinput
   ```
5. Start Command:
   ```
   gunicorn casa_fuego.wsgi
   ```
6. Added Render URL to ALLOWED_HOSTS  
7. Deployed successfully  
8. Static files handled by Whitenoise  

---

# **9. Credits**

### **Content**
- Menu content written by developer  
- Google Fonts used for typography  

### **Code**
- Django documentation  
- StackOverflow for debugging  
- Code Institute resources

# **10. Security**
- DEBUG disabled in production  
- Secret key stored in environment variables  
- Authentication required for booking management  
- Form validation on all fields  

---

# **11. Screenshots**

- Homepage  
![Homepage Screenshot](/casa_fuego/bookings/static/images/homepage.png)
- Booking form  
![Booking Screenshot](/casa_fuego/bookings/static/images/booking.png)
- Menu page 
![Menu Screenshot](/casa_fuego/bookings/static/images/menu.png)
- Booking success 
![Booking Success Screenshot](/casa_fuego/bookings/static/images/booking-success.png)
- My bookings 
![My Bookings Screenshot](/casa_fuego/bookings/static/images/my-bookings.png)
- Login / Signup
![Login/Signup Screenshot](/casa_fuego/bookings/static/images/login.png) ![Homepage Screenshot](/casa_fuego/bookings/static/images/signup.png)
# **Thank You**

This project was developed as part of the Code Institute Full-Stack Software Development course.