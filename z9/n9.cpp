#include<string>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<Eigen/Dense>
using namespace Eigen;

void powIteration(Matrix3d* m, double* eVals) {
	VectorXd out(3), tmp(3);
	double prevFactor = 0;
	VectorXd vec(3);
	vec<< 1, 1, 1;	//losowy wektor, wybrałem [1,1,1]
	float currentFactor;
	int counter = 0;
	for(int i = 0 ; i<3;i++) {
		while(true) {
			std::cout<<"counter = "<<counter<<std::endl;
			out = *m * vec;
			out /= out.norm();
			tmp = *m * out;
			currentFactor = out.dot(tmp);
			vec = out;
			std::cout<<fabs(prevFactor-currentFactor)<<std::endl;
			std::cout<<"lambda "<<i<<" = "<<prevFactor<<std::endl;
			if(fabs(prevFactor-currentFactor) <= 1e-8) {
					eVals[i] = prevFactor;
				vec <<1,1,1;
				break;

			}
			prevFactor = currentFactor;
			counter++;
		}	// jako ,że A = suma po i lambda(i) * eigenvector(i) * eigenvector(i) transponowany
			//zrobimy tak,żeby lambda(i) się zerowała i obliczymy następne lambda
		*m = *m - (prevFactor * out*out.transpose());
		counter=0;
		std::cout<<*m<<std::endl;
	}
}
void RayleighIteration(Matrix3d* m, double* eVals) {

	VectorXd out(3);
	double prevFactor = 30; //jakaś wartość poczatkowa, niech bedzie 30
	VectorXd vec(3);
	vec<< 1, 1, 1;	//losowy wektor, wybrałem [1,1,1]
	float currentFactor;
	int counter = 0;
	for(int i = 0 ; i<2;i++) {
		while(true) {
			std::cout<<"counter = "<<counter<<std::endl;
			out = (*m -prevFactor*Matrix3d::Identity()).inverse()* vec;
			out /= out.norm();
			currentFactor = vec.dot(*m*vec)/vec.dot(vec);
			vec = out;
			std::cout<<fabs(prevFactor-currentFactor)<<std::endl;
			std::cout<<"lambda "<<i<<" = "<<prevFactor<<std::endl;
			if(fabs(prevFactor-currentFactor) <= 1e-8) {
					eVals[i] = prevFactor;
				vec <<1,1,1;
				break;

			}
			prevFactor = currentFactor;
			counter++;
		}
		counter = 0;
		if(i == 0)// Trace(A) = suma wartosci wlasnych.Szacujemy przyblizenie drugiej
			prevFactor = m->trace() - prevFactor;
		if(i == 1)	// ostatnia wyliczamy odejmujac od trace(A) 2 pozostale wartosci wlasne
			eVals[2] = m->trace() - eVals[0] - eVals[1];
		std::cout<<*m<<std::endl;
	}
}
void iterativeQR(Matrix3d* m, double* eVals) {
	Matrix3d Bprev = *m, Bcurrent = Matrix3d::Identity(),Q,R;
	int counter=0;
	while(true) {
		Q = Bprev.colPivHouseholderQr().matrixQ();
		R = Q.inverse() * Bprev;
		Bcurrent = R * Q;
		if(fabs(Bcurrent(0) - Bprev(0)) <= 1e-8)
			break;
		Bprev = Bcurrent;
		counter++;
	}
	for(int i=0;i<3;i++)
		eVals[i] = Bcurrent(i*3 +i);
}
void initMatrix(Matrix3d* m) {
	*m <<	1, 2, 3,
		2, 4, 5,
		3, 5, -1;
}
int main () {
	//macierz zapisana column wise
	std::string labels[3] = {"Potegowa", "Rayleigha", "QR"};
	Matrix3d* A = new Matrix3d();
	initMatrix(A);
	std::cout<<*A<<std::endl;
	double eigVals[9] = {0}; //tablica przechowujaca wartosci wlasne liczone
						//3 metodami,w sumie 9
	//potegowa
	powIteration(A, eigVals);
	//Rayleigha
	initMatrix(A);
	RayleighIteration(A, eigVals+3);

	//QR
	initMatrix(A);
	iterativeQR(A, eigVals+6);
	std::cout<<"Wartosci wlasne: "<<A->eigenvalues()<<std::endl;
	for(int i=0;i<3;i++) {
		std::cout<<labels[i]<<std::endl;
		for(int j=0;j<3;j++)
			std::cout<<eigVals[i*3 +j]<<std::endl;
	}
}
