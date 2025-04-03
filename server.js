const db = require("./firebase");

// Test Firebase connection
db.collection("test").add({ message: "Hello Firebase!" })
  .then(() => console.log("✅ Firebase is connected!"))
  .catch((error) => console.error("❌ Firebase error:", error));
