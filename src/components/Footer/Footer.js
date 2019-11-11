import React from "react";
import "./Footer.scss";

export const Footer = () => {
    return (
        <footer className="footer">
            <div className="content">
                <div className="footer__top-part">
                    <div className="footer__main">
                        <div className="fotter__logo-container">
                            <img 
                                className="footer__logo"
                                src="./images/logo.svg" 
                                alt="Campus Nutrition" 
                            />
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    )
};
