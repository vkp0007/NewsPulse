import MainLayout from "./components/layout/MainLayout";
import AppRoutes from "./routes/AppRoutes";
console.log("App rendered");

function App() {
    return (
        <MainLayout>
            <AppRoutes />
        </MainLayout>
    );
}

export default App;