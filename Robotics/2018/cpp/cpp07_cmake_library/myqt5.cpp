#include "myqt5.h"
void myqt_func(const char* str) {
	QString qstr = str;
	qDebug() << "myqt5" << qstr;
}
