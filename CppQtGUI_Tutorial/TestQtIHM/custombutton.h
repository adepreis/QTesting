#ifndef CUSTOMBUTTON_H
#define CUSTOMBUTTON_H

#include <QObject>
#include <QPushButton>

class CustomButton : public QPushButton
{
    Q_OBJECT    // Ajouté

public:
    CustomButton(QWidget* parent = 0);  // Modifié
    ~CustomButton();       // added
};

#endif // CUSTOMBUTTON_H
