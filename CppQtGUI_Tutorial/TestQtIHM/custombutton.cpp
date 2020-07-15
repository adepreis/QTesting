#include "custombutton.h"
#include <QPushButton>

#include <QDebug>   // added

CustomButton::CustomButton(QWidget *parent)
    : QPushButton(parent)       // Modifié
{
    setText("Bonjour !");
}

CustomButton::~CustomButton()      // added
{
    qDebug() << "Destruction !" << endl;
}
