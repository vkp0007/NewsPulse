import Hero from "../components/home/Hero";
import Pipeline from "../components/home/Pipeline";
import Footer from "../components/home/Footer";

function Home() {
  return (
    <div className="space-y-20">
      <Hero />
      <Pipeline />
      <Footer />
    </div>
  );
}

export default Home;