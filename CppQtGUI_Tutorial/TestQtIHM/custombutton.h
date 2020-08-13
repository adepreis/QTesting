#ifndef CUSTOMBUTTON_H
#define CUSTOMBUTTON_H

#include <QObject>
#include <QPushButton>
#include <QTimer>

class CustomButton : public QPushButton
{
    Q_OBJECT

private slots :
    void btnAction();
    void disableButton();

public:
    CustomButton(int lifetime, QString text, QWidget* parent = 0);
    ~CustomButton();

private:
    QTimer timer;
};

#endif // CUSTOMBUTTON_H
