import React from "react"
import { Routes, Route } from "react-router-dom"
import Login from "./pages/login"
import ChatBox from "./components/ChatBox"

const App = () => {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/" element={<ChatBox />} />
    </Routes>
  )
}

export default App