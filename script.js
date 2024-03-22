function handleSignupForm(event) {
    event.preventDefault();  // Prevent form submission

    // Get form input values
    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;
    let password = document.getElementById('password').value;

    // Create user data object
    let userData = {
        name: username,
        email: email,
        password: password,
        token: null,
        active_or_blocked: 'active',
        phone: phone,
        last_login: null
    };

    for (let key in userData) {
        if (userData.hasOwnProperty(key)) {
            let value = userData[key];
            console.log(`${key}: ${value}`);
        }
    }

    // Send POST request to backend
    fetch('http://localhost:8003/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Signup successful:', data);
        if (data && data.message && data.message === "User signed up successfully") {
            window.location.pathname = "/dashboard.html";
        }       
        // Optionally, perform any actions after successful signup
    })
    .catch(error => {
        console.error('Signup failed:', error);
        // Optionally, display an error message to the user
    });
}


// get user with id
function get_user(id) {
fetch('http://127.0.0.1:8001/users/{id}')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Handle the data returned from the API
    console.log(data);
    // Now you can use the data in your JavaScript code
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
  });
}

//get all users
function get_users() {
fetch('http://127.0.0.1:8001/all-users')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Handle the data returned from the API
    // console.log(data);
    return data;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
  });
}


function handleProductUpload(event) {
    event.preventDefault();  // Prevent form submission

    // Get form input values
    let title = document.getElementById('Pproduct_name').value;
    let description = document.getElementById('Pdescription').value;
    let product_category = document.getElementById('Pproduct_category').value;
    let location = document.getElementById('Plocation').value;
    let price = document.getElementById('Pprice').value;
    // const fileInput = document.getElementById('image');

    // Create product data object
    let productData = {
        title: title,
        description: description,
        category: product_category,
        location: location,
        price: price,
        favcolor: 'none',
        image: 'null',
        likes: 0,
        seller_id: 1,
        reported: 0,
        whatsapp_visits: 0,
    };

    for (let key in productData) {
        if (productData.hasOwnProperty(key)) {
            let value = productData[key];
            console.log(`${key}: ${value}`);
        }
    }

    console.log(productData);

    // Send POST request to backend
    fetch('http://localhost:8003/product', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(productData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('product upload successful:', data);
        if (data && data.message && data.message === "Product uploaded successfully.") {
            window.location.pathname = "/dashboard.html";
        }       
        // Optionally, perform any actions after successful upload
    })
    .catch(error => {
        console.error('Product upload failed:', error);
        // Optionally, display an error message to the user
    });
}

  
// upload image
function uploadImage(fileInput) {
  const file = fileInput.files[0];
  
  const formData = new FormData();
  formData.append('image', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Network response was not ok.');
  })
  .then(data => {
    console.log('Image uploaded successfully:', data);
  })
  .catch(error => {
    console.error('There was a problem with the image upload:', error);
  });
}

// blog
function handleBlogs(event) {
    event.preventDefault();  // Prevent form submission

    // Get form input values
    let color = document.getElementById('BGfavcolor').value;
    let title = document.getElementById('BGtitle').value;
    let subtitle = document.getElementById('BGsubtitle').value; 
    let category = document.getElementById('BGblog_category').value; 
    let blog = document.getElementById('BGblog').value; 
  
    let housetorentData = {
        title: title,
        color: color,
        subtitle: subtitle,
        category: category,
        blog: blog,
        likes: 0,
        forwards: 0,
        seller_id: 1,
    };

    for (let key in housetorentData) {
        if (housetorentData.hasOwnProperty(key)) {
            let value = housetorentData[key];
            console.log(`${key}: ${value}`);
        }
    }

    console.log(housetorentData);

    // Send POST request to backend
    fetch('http://localhost:8003/Blogs', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(housetorentData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('podcast upload successful:', data);
        if (data && data.message && data.message === "Blogs uploaded successfully.") {
              window.location.pathname = "/blogs.html";
        }       
        // Optionally, perform any actions after successful upload
    })
    .catch(error => {
        console.error('Accomodation upload failed:', error);
        // Optionally, display an error message to the user
    });
}


//Ads
function handleAds(event) {
    event.preventDefault();  // Prevent form submission

    // Get form input values
    let color = document.getElementById('ADfavcolor').value;
    let title = document.getElementById('ADtitle').value;
    let link = document.getElementById('ADlink').value; 

  
    let housetorentData = {
        title: title,
        color: color,
        link: link,
        clicks: 0,
        seller_id: 1,
    };

    for (let key in housetorentData) {
        if (housetorentData.hasOwnProperty(key)) {
            let value = housetorentData[key];
            console.log(`${key}: ${value}`);
        }
    }

    console.log(housetorentData);

    // Send POST request to backend
    fetch('http://localhost:8003/Ads', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(housetorentData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('podcast upload successful:', data);
        if (data && data.message && data.message === "Ads uploaded successfully.") {
              window.location.pathname = "/dashboard.html";
        }       
        // Optionally, perform any actions after successful upload
    })
    .catch(error => {
        console.error('Accomodation upload failed:', error);
        // Optionally, display an error message to the user
    });
}

// memories and happeninges
function handleMemories(event) {
    event.preventDefault();  // Prevent form submission

    // Get form input values
    let text = document.getElementById('MEblog').value;
    let category = document.getElementById('MEcategory').value;

  
    let housetorentData = {
        text: text,
        category: category,
        likes: 0,
        dislikes: 0,
        seller_id: 1,
    };

    for (let key in housetorentData) {
        if (housetorentData.hasOwnProperty(key)) {
            let value = housetorentData[key];
            console.log(`${key}: ${value}`);
        }
    }

    console.log(housetorentData);

    // Send POST request to backend
    fetch('http://localhost:8003/Memories', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(housetorentData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('podcast upload successful:', data);
        if (data && data.message && data.message === "Memories uploaded successfully.") {
              window.location.pathname = "/memories.html";
        }       
        // Optionally, perform any actions after successful upload
    })
    .catch(error => {
        console.error('Accomodation upload failed:', error);
        // Optionally, display an error message to the user
    });
}

// house to rent
function handleHouseToRent(event) {
    event.preventDefault();  // Prevent form submission

    // Get form input values
    let name = document.getElementById('Hhouse_name').value;
    let description = document.getElementById('Hdescription').value;
    let category = document.getElementById('Hcategory').value;
    let price = document.getElementById('Hprice').value;
    let vacant = document.getElementById('HVacant').value;
  
    let housetorentData = {
        name: name,
        description: description,
        category: category,
        price: price,
        vacant: vacant,
        seller_id: 1,
    };

    for (let key in housetorentData) {
        if (housetorentData.hasOwnProperty(key)) {
            let value = housetorentData[key];
            console.log(`${key}: ${value}`);
        }
    }

    console.log(housetorentData);

    // Send POST request to backend
    fetch('http://localhost:8003/Housetorent', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(housetorentData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('podcast upload successful:', data);
        if (data && data.message && data.message === "Accomodation uploaded successfully.") {
              window.location.pathname = "/Accomodation.html";
        }       
        // Optionally, perform any actions after successful upload
    })
    .catch(error => {
        console.error('Accomodation upload failed:', error);
        // Optionally, display an error message to the user
    });
}

// entertainment
function handlePodcastUpload(event) {
    event.preventDefault();  // Prevent form submission

    // Get form input values
    let title = document.getElementById('pdtitle').value;
    let description = document.getElementById('pddescription').value;
    let category = document.getElementById('pdcategory').value;
    let favcolor = document.getElementById('pdfavcolor').value;
    let link = document.getElementById('pdlink').value;
  
    // Create podcast data object
    let podcastData = {
        title: title,
        description: description,
        category: category,
        color: favcolor,
        likes: 0,
        link: link,
        seller_id: 1,
    };

    for (let key in podcastData) {
        if (podcastData.hasOwnProperty(key)) {
            let value = podcastData[key];
            console.log(`${key}: ${value}`);
        }
    }

    console.log(podcastData);

    // Send POST request to backend
    fetch('http://localhost:8003/podcast', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(podcastData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('podcast upload successful:', data);
        if (data && data.message && data.message === "Entertainment uploaded successfully.") {
              window.location.pathname = "/entertainment.html";
        }       
        // Optionally, perform any actions after successful upload
    })
    .catch(error => {
        console.error('Podcast upload failed:', error);
        // Optionally, display an error message to the user
    });
}

// education
function handleEducationUpload(event) {
      event.preventDefault();  // Prevent form submission

      // Get form input values
      let title = document.getElementById('edtitle').value;
      let subtitle = document.getElementById('edsubtitle').value;
      let description = document.getElementById('eddescription').value;
      let category = document.getElementById('edcategory').value;
      // let link = document.getElementById('edlink').value;
      let favcolor = document.getElementById('edfavcolor').value;

      // Create education data object
      let educationData = {
          title: title,
          subtitle: subtitle,
          blog: description,
          category: category,
          color: favcolor,
          likes: 0,
          forwards: 0,
          seller_id: 1,
      };

      console.log(educationData);

      // Send POST request to backend
      fetch('http://localhost:8003/uploadEducation', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(educationData)
      })
      .then(response => response.json())
      .then(data => {
          console.log('education upload successful:', data);
          if (data && data.message && data.message === "Education uploaded successfully.") {
              window.location.pathname = "/education.html";
          }       
          // Optionally, perform any actions after successful upload
      })
      .catch(error => {
          console.error('Education upload failed:', error);
          // Optionally, display an error message to the user
      });
  }