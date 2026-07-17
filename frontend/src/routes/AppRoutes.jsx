import { Routes, Route } from "react-router";

import Dashboard from "../pages/Dashboard";
import ClusterDetails from "../pages/ClusterDetails";
import ArticleDetails from "../pages/ArticleDetails";

import NotFound from "../pages/NotFound";
import Home from "../pages/Home";

function AppRoutes() {
    return (
        <Routes>

    <Route path="/" element={<Home />} />

    <Route path="/dashboard" element={<Dashboard />} />

    <Route path="/clusters/:id" element={<ClusterDetails />} />

    <Route path="/articles/:id" element={<ArticleDetails />} />


    <Route path="*" element={<NotFound />} />

</Routes>
    );
}

export default AppRoutes;