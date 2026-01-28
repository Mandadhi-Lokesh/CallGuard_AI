import { Routes, Route } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Home } from './pages/Home';
import { Analyzer } from './pages/Analyzer';
import { Result } from './pages/Result';
import { About } from './pages/About';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/analyzer" element={<Analyzer />} />
        <Route path="/result" element={<Result />} />
        <Route path="/impact" element={<About />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Layout>
  );
}

export default App;
