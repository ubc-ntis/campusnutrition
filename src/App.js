import React from "react";
import { Provider } from "react-redux";
import "./App.scss";
import { store } from "./store";
import { RestaurantsListPage } from "./components/RestaurantsListPage/";
import { Header } from "./components/Header/Header";
import { Footer } from "./components/Footer/Footer"

export const App = () => (
    <Provider store={store}>
        <div className="page">
            <Header />
            <main className="content">
                <RestaurantsListPage />
            </main>
            <Footer />
        </div>
    </Provider>
);
