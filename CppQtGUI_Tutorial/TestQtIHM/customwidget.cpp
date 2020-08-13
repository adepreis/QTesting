#include "customwidget.h"
#include <QPainter>

CustomWidget::CustomWidget(QWidget *parent) : QWidget(parent)
{
    setMinimumWidth(50);
}

void CustomWidget::paintEvent(QPaintEvent* event)
{
    QPainter p(this);

    // modify border color on click
    p.setPen(isClicked ? Qt::blue : Qt::black);

    p.setBrush(Qt::gray);

    p.drawRoundedRect(0, 0, this->width(), this->height(), 10, 10);

    // optional : text in the widget...

//    updateGeometry();   // good practice ? should recalculates the space occupied by the widget..
}

void CustomWidget::mousePressEvent(QMouseEvent *e)
{
    isClicked = true;
    repaint();  // forces widget to update its appearance
}

void CustomWidget::mouseReleaseEvent(QMouseEvent *e)
{
    isClicked = false;
    repaint();  // forces widget to update its appearance
}
