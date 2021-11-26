import { render, screen } from '@testing-library/react';
import App from './App';
import React from 'react';
import App from './App';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import { Provider } from 'react-redux' //ini tambahin provider bwt nyimpan data global
import store from './store';


test('renders learn react link', () => {
  render(
    <React.StrictMode>
      <Provider store={store}>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<App />} >
              <Route path="/" element={<Home />} />
              <Route path="contact" element={<Contact />} />
              <Route path="about" element={<About />}>
                <Route path="me" element={<Contact />} />
              </Route>
            </Route>

          </Routes>
        </BrowserRouter>
      </Provider>
    </React.StrictMode>
  );
  const linkElement = screen.getByText(/^add by 1$/i);
  //
  //
  //
  expect(linkElement).toBeInTheDocument();
});
