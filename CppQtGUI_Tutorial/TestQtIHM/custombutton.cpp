#include "custombutton.h"
#include <QPushButton>
#include <QMessageBox>

#include <QDebug>   // added

CustomButton::CustomButton(QString text, QWidget *parent)
    : QPushButton(parent)       // Modifié
{
    setText(text);
}

void CustomButton::btnAction()
{
    QMessageBox::information(this, "Titre","Clic détécté !");
}

CustomButton::~CustomButton()      // added
{
    qDebug() << "Destruction !" << endl;
}
