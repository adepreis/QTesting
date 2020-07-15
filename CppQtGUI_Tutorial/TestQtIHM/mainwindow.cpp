#include "mainwindow.h"
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    setWindowTitle("Ma super application !");

    m_hBoxLayout = new QHBoxLayout(this);

    m_mainWidget = new QWidget(this);       // prend en parent this pour l'auto destruction
    m_mainWidget->setLayout(m_hBoxLayout);  // le layout principal sera le HBox

    m_vBoxLayout = new QVBoxLayout(this);   // création du VBox

    m_hBoxLayout->addLayout(m_vBoxLayout);  // ajout du VBox dans le HBox

    m_customBtnBonjour = new CustomButton(this);
    /*
        Méthode pour "linker" un bouton et une fonction (DP Observer) :
        m_customBtnBonjour,     bouton que l'on souhaite "binder"
        SIGNAL(clicked(bool)),  type de l'evenement à écouter
        this,                   Objet auquel est associé la fonction
        SLOT(onClickCustomBtn(bool))    la fonction en question
    */
    connect(m_customBtnBonjour, SIGNAL(clicked(bool)), this, SLOT(onClickCustomBtn()));

    m_hBoxLayout->addWidget(m_customBtnBonjour);    // ajout du btn dans le HBOX

    for(int i=0; i<10; i++)
        m_vBoxLayout->addWidget(new QPushButton("Bla", m_mainWidget));      // ajout de plsr btn dans VBOX

    setCentralWidget(m_mainWidget);     // spécifie le widget principal
}

MainWindow::~MainWindow()
{

}

void MainWindow::onClickCustomBtn() {
    qDebug() << "Clic détecté sur le btn Bonjour" << endl;;
}
