# Access Control Attendance System

## Project Overview
The **Access Control Attendance System** is a robust, Python-based application designed to manage and monitor access control and attendance records efficiently. This project leverages face recognition technology for authentication and attendance tracking, providing a seamless and secure solution for organizations.

---

## Features

1. **Face Recognition-Based Access Control**:
   - Real-time detection and recognition of faces using a camera feed.
   - Grant or deny access based on pre-registered user data.

2. **Dataset Management**:
   - Easily create and manage datasets for user registration.
   - Train models to encode facial features for efficient recognition.

3. **Attendance Tracking**:
   - Automatic attendance marking upon successful authentication.
   - Attendance records stored in CSV files for easy access and analysis.

4. **Access Logs**:
   - Maintain detailed logs of access events for enhanced security.

5. **Intuitive GUI**:
   - User-friendly graphical interface for controlling and monitoring the system.

---

## Installation

### Prerequisites
- Python 3.7+
- pip
- A compatible camera module
- Libraries and dependencies (see below)

### Clone the Repository
```bash
git clone https://github.com/yourusername/ACCESS-CONTROL-ATTENDANCE-SYSTEM.git
cd ACCESS-CONTROL-ATTENDANCE-SYSTEM
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

Required libraries include:
- `opencv-python`
- `numpy`
- `pandas`
- `pillow`
- `tkinter` (built-in with Python)

---

## Usage

### Running the Application
1. Launch the main application:
   ```bash
   python start.py
   ```
2. Use the GUI to:
   - Create datasets
   - Train the dataset
   - Recognize faces for access control
   - View attendance records

### Dataset Creation
- Add new users by running the "Create Dataset" feature, which captures multiple images of a user and stores them for training.

### Training the Model
- Train the face recognition model using the "Train Dataset" feature to encode facial features.

### Real-Time Recognition
- Start the "Recognize + Access Control" feature to authenticate users and log attendance in real-time.

### Access Attendance Records
- View attendance sheets directly through the GUI or access the CSV files stored in the `CSV_sheet` folder.

---

## Project Structure
```plaintext
ACCESS-CONTROL-ATTENDANCE-SYSTEM/
├── dataset_creator.py       # Script for creating user datasets
├── Find_Encodings.py        # Script for training face encodings
├── Detection_and_Recognition_LIVE.py  # Script for real-time face recognition
├── start.py                 # Main application script
├── CSV_sheet/               # Folder for storing attendance sheets
├── icons/                   # Icons for the GUI
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
```

---

## Screenshots
![GUI Screenshot](path_to_screenshot)

---

## Contributing
1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---



---

## Acknowledgements
- OpenCV and Python for providing the foundation for computer vision.
- The Python community for developing the amazing libraries used in this project.

---

## Contact

- **Email**: pragatirpehrkar@gmail.com
- **GitHub**: [Prari2725](https://github.com/Prari2725)
