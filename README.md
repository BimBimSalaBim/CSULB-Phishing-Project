
# Phishing Project

## Overview

This project aims to demonstrate the creation and implementation of a phishing attack as part of a security awareness exercise. The project is intended for educational purposes to highlight the vulnerabilities and potential consequences of phishing attacks. The primary goal is to educate students and faculty at California State University Long Beach (CSULB) about phishing threats and how to identify and avoid them.

## Table of Contents

- [What is Phishing?](#what-is-phishing)
- [Project Overview](#project-overview)
- [Convincing Website](#convincing-website)
- [Website Login](#website-login)
- [Emailing](#emailing)
- [Connecting It All](#connecting-it-all)
- [Testing](#testing)
- [Conclusion](#conclusion)
- [Appendix](#appendix)
- [References](#references)

## What is Phishing?

Phishing is a type of cybercrime that involves tricking recipients into revealing personal information by pretending to be a trustworthy entity. The attackers use spoofed emails and fraudulent websites to steal information. The history of phishing dates back to the 1990s with attacks targeting America Online (AOL) users.

## Project Overview

### Contributions of Team Members

- **Carine Gordillo**: Lead front-end developer, managed and designed the website.
- **Rushil Prajapati**: Full-stack developer, established connections between front and back-end, conducted back-end testing using Flask.
- **Twan Tran**: Full-stack developer, implemented front-end and back-end integration, enabled user interactions through the UI.
- **Aveline Villaganas**: Full-stack developer, designed phishing emails, developed an algorithm to send mass emails.
- **Faizan Zafar**: Project manager, served as lead back-end developer and server admin,created deliverables and tracking schedules.

### Target Audience

- **Students of CECS 378**: Targeted using student emails on Microsoft Outlook.
- **Faculty of CSULB**: Targeted using faculty emails on Microsoft Outlook.

### Goals

- **Students**: Pose as CSULB Enrollment Services and send urgent emails about account holds.
- **Faculty**: Pose as the Office of Enrollment Services and send emails about student withdrawal requests.

### Information Handling

- Store email usernames and phone numbers in a text document.
- Change passwords of faculty members.

## Convincing Website

To deceive users effectively, the project involved creating a convincing domain name and website closely resembling legitimate CSULB services. Despite initial challenges with phishing flags, the website was successfully hosted and approved after appealing to Google.

## Website Login

The login page was meticulously crafted to mirror the CSULB Single Sign-On portal. Initial attempts at direct HTML copying were unsuccessful, leading to the development of a new structure. Issues with mobile responsiveness were identified and addressed later in the development process.

## Emailing

The project involved creating realistic email templates posing as CSULB Enrollment Services. Scripts were developed to automate the sending of these emails, customizing each message with the recipient's first name. Tools like Sendinblue and the `sendemail` program were used to ensure emails were delivered securely and appeared legitimate.

## Connecting It All

The project utilized Selenium Webdriver, Flask, and Google Cloud to automate the phishing attack. Challenges with Apache led to the adoption of Flask for server-client communication. Multiple threading was implemented to handle simultaneous user interactions. The project's success hinged on integrating various tools and techniques to achieve a convincing phishing attack.

## Testing

Initial testing revealed issues with server stability under multiple logins, which were addressed with threading fixes. Over several rounds of email launches, the project successfully captured sensitive information from multiple users.

## Conclusion

The project demonstrated the effectiveness of phishing attacks and underscored the importance of awareness and education in cybersecurity. Despite sophisticated web and graphic design techniques, small giveaways can still betray a phishing attempt. The project highlights the need for continuous efforts in cybersecurity education.

## Appendix

- **Concatenate**: To link or join together.
- **MiTM**: Man-in-the-Middle attack.
- **Spoofing**: Imitating a legitimate source to deceive recipients.
- **SMTP**: Send Mail Transfer Protocol, standard for sending emails on the Internet.

## References

- [KnowBe4: History of Phishing](https://www.phishing.org/history-of-phishing)
- [Microsoft Support: What is phishing?](https://support.microsoft.com/en-us/windows/protect-yourself-from-phishing-0c7ea947-ba98-3bd9-7184-430e1f860a44)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Selenium Webdriver Documentation](https://github.com/SeleniumHQ/selenium/tree/trunk/javascript/node/selenium-webdriver#readme)
