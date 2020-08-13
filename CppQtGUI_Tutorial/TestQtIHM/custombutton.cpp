#include "custombutton.h"
#include <QPushButton>
#include <QMessageBox>

#include <QDebug>

CustomButton::CustomButton(int lifetime, QString text, QWidget *parent)
    : QPushButton(parent)
{
    setText(text);

    // Connect a timer that disable the button after the lifetime specified
    timer.setInterval(lifetime);
    timer.start();
    connect(&timer, SIGNAL(timeout()), this, SLOT(disableButton()));
}

void CustomButton::btnAction()
{
    QMessageBox::information(this, "Titre", "Clic détécté !");
}

CustomButton::~CustomButton()
{
    qDebug() << "Destruction !" << endl;
}

void CustomButton::disableButton()
{
    setText("Trop tard");
    setEnabled(false);
    timer.stop();
}
