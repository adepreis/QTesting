#include "customwidget.h"
#include <QPainter>

CustomWidget::CustomWidget(QWidget *parent) : QWidget(parent)
{
    setMinimumWidth(50);
}

void CustomWidget::paintEvent(QPaintEvent* event)
{
    QPainter p(this);

    p.setPen(isClicked ? Qt::blue : Qt::black);     // contour modifié si cliqué

    p.setBrush(Qt::gray);

    p.drawRoundedRect(0, 0, this->width(), this->height(), 10, 10);

    // facultatif : texte dans le widget...

//    updateGeometry();   // bonne pratique ? recalcule l'espace occupé par le widget
}

void CustomWidget::mousePressEvent(QMouseEvent *e)
{
    isClicked = true;
    repaint();  // force le widget à mettre à jour son apparence
}

void CustomWidget::mouseReleaseEvent(QMouseEvent *e)
{
    isClicked = false;
    repaint();  // force le widget à mettre à jour son apparence
}
