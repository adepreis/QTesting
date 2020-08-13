#include "mainwindow.h"
#include <QDebug>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent)
{
    setWindowTitle("Ma super application !");

    m_hBoxLayout = new QHBoxLayout(this);

    m_mainWidget = new QWidget(this);       // takes "this" as a parent (for self-destruction)
    m_mainWidget->setLayout(m_hBoxLayout);  // main layout will be the HBox

    m_vBoxLayout = new QVBoxLayout(this);   // VBox creation

    m_hBoxLayout->addLayout(m_vBoxLayout);  // adds VBox in the HBox

    m_customBtnBonjour = new QPushButton("Pouet pouet", this);
    m_customBtnBonjour->setSizePolicy(QSizePolicy::Maximum, QSizePolicy::Minimum);
    /*
        Method to "link" a button and a function (DP Observer) :
        m_customBtnBonjour,     button that we want to "bind"
        SIGNAL(clicked(bool)),  type of the event to listen to
        this,                   Object associated to the following function
        SLOT(onClickCustomBtn(bool))    the triggered function
    */
    connect(m_customBtnBonjour, SIGNAL(clicked(bool)), this, SLOT(onClickCustomBtn()));

    m_hBoxLayout->addSpacing(20);
    m_hBoxLayout->addWidget(m_customBtnBonjour);    // adds btn in the HBox
    m_hBoxLayout->addWidget(new CustomWidget());

    for(int i=0; i<10; i++) {
        int msBeforeBeingDisabled = i * 2000;
        CustomButton* tempButton = new CustomButton(msBeforeBeingDisabled, "Bonjour !", m_mainWidget);
        m_vBoxLayout->addWidget(tempButton);      // adds multiples btn in the VBOX

        connect(tempButton, SIGNAL(clicked(bool)), tempButton, SLOT(btnAction()));
    }

    setCentralWidget(m_mainWidget);     // specified the main widget
}

MainWindow::~MainWindow()
{

}

void MainWindow::onClickCustomBtn() {
    qDebug() << "Clic détecté sur le bouton" << m_customBtnBonjour->text() << endl;

}
